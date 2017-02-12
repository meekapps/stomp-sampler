//
//  ApiRequest.m
//  stomp-sampler
//
//  Created by Mike Keller on 2/10/17.
//  Copyright © 2017 Perka. All rights reserved.
//

#import "ApiRequest.h"

@interface ApiRequest()
@property (nonatomic) HttpMethod method;
@property (copy, nonatomic) NSString *path;
@property (strong, nonatomic) NSData *formData;
@end

static NSString *const kApiServerBase = @"http://192.168.1.5:5000";

@implementation ApiRequest

- (instancetype) initWithMethod:(HttpMethod)method
                           path:(NSString*)path
                       formData:(NSData*)formData {
  self = [super init];
  if (self) {
    self.method = method;
    self.path = path;
    self.formData = formData;
  }
  return self;
}

- (instancetype) initWithMethod:(HttpMethod)method
                           path:(NSString*)path {
  return [self initWithMethod:method path:path formData:nil];
}

- (instancetype) initWithPath:(NSString*)path {
  return [self initWithMethod:HttpMethodGet path:path];
}

- (void) baseExecuteWithCompletion:(ApiRequestCompletion)completion {
  [self performRequestWithMethod:self.method
                            path:self.path
                        formData:self.formData
                      completion:^(id result) {
                        id deserialized = [self deserialize:result];
                        if (completion) completion(deserialized);
                      }];
}

- (id) deserialize:(id)result {
  return result;
}

#pragma mark - Private

- (void) performRequestWithMethod:(HttpMethod)method
                             path:(NSString*)path
                         formData:(NSData*)formData
                       completion:(ApiRequestCompletion)completion {
  
  NSString *fullPath = [self fullPathWithPath:path];
  NSURL *url = [NSURL URLWithString:fullPath];
  NSMutableURLRequest *request = [NSMutableURLRequest requestWithURL:url];
  
  NSString *httpMethod = [self httpMethod:method];
  request.HTTPMethod = httpMethod;
  
  NSString *contentType = formData ? @"multipart/form-data" : @"application/json";
  [request setValue:contentType forHTTPHeaderField:@"Content-Type"];
  
  if (formData) {
    NSMutableData *body = [NSMutableData data];
    [body appendData:formData];
    [request setHTTPBody:body];
  }
  
  NSURLSession *session = [NSURLSession sharedSession];
  NSURLSessionDataTask *dataTask =
  [session dataTaskWithRequest:request completionHandler:^(NSData * _Nullable data,
                                                           NSURLResponse * _Nullable response,
                                                           NSError * _Nullable error) {
    if (!error) {
      id json = [NSJSONSerialization JSONObjectWithData:data
                                                options:kNilOptions
                                                  error:nil];
      if (completion) {
        dispatch_async(dispatch_get_main_queue(), ^{
          NSLog(@"\n***RESPONSE****\n%@ %@\n%@\n\n", httpMethod, path, json);
          completion(json);
        });
      }
    }
  }];
  
  NSLog(@"\n***REQUEST***\n%@ %@\n(Content-Type: %@)\n\n", httpMethod, fullPath, contentType);
  
  [dataTask resume];
}

- (NSString*) fullPathWithPath:(NSString*)path {
  return [NSString stringWithFormat:@"%@%@", kApiServerBase, path];
}

- (NSString*) httpMethod:(HttpMethod)method {
  switch (method) {
    case HttpMethodGet:
      return @"GET";
      break;
    case HttpMethodDelete:
      return @"DELETE";
      break;
    case HttpMethodPost:
      return @"POST";
    default:
      return nil;
      break;
  }
}

@end
