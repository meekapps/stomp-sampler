//
//  ApiRequest.h
//  stomp-sampler
//
//  Created by Mike Keller on 2/10/17.
//  Copyright © 2017 Perka. All rights reserved.
//

@import UIKit;

typedef NS_ENUM(NSUInteger, HttpMethod) {
  HttpMethodGet,
  HttpMethodDelete,
  HttpMethodPost
};

typedef void(^ApiRequestCompletion)(id result);

@protocol ApiRequestProtocol <NSObject>

@required
- (id) deserialize:(id)result;

@end

@interface ApiRequest : NSObject

- (instancetype) initWithMethod:(HttpMethod)method
                           path:(NSString*)path
                       formData:(NSData*)data;

- (instancetype) initWithMethod:(HttpMethod)method
                           path:(NSString*)path;

- (instancetype) initWithPath:(NSString*)path;

- (void) baseExecuteWithCompletion:(ApiRequestCompletion)completion;

- (id) deserialize:(id)result;

@end
