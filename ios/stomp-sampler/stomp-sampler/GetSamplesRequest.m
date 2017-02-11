//
//  GetSamplesRequest.m
//  stomp-sampler
//
//  Created by Mike Keller on 2/10/17.
//  Copyright © 2017 Perka. All rights reserved.
//

#import "GetSamplesRequest.h"
#import "Sample.h"

@implementation GetSamplesRequest

- (instancetype) init {
  self = [super initWithMethod:HttpMethodGet
                          path:@"/samples"];
  if (self) {}
  return self;
}

- (void) executeWithCompletion:(GetSamplesCompletion)completion {
  [self baseExecuteWithCompletion:^(id result) {
    if (completion) completion(result);
  }];
}

#pragma mark - Private

- (NSArray<Sample*>*) deserialize:(id)result {
  id samples = result[@"samples"];
  if (!samples) return nil;
  
  if (![samples conformsToProtocol:@protocol(NSFastEnumeration)]) return nil;
  
  NSMutableArray *mutableSamples = [NSMutableArray array];
  for (id s in samples) {
    Sample *sample = [[Sample alloc] initWithFilename:s];
    [mutableSamples addObject:sample];
  }
  
  return [mutableSamples copy];
}

@end
