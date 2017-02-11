//
//  SamplesRequest.m
//  stomp-sampler
//
//  Created by Mike Keller on 2/11/17.
//  Copyright © 2017 Perka. All rights reserved.
//

#import "Sample.h"
#import "SamplesRequest.h"

@implementation SamplesRequest

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

- (void) executeWithCompletion:(SamplesCompletion)completion {
  [self baseExecuteWithCompletion:^(id result) {
    if (completion) completion(result);
  }];
}

@end
