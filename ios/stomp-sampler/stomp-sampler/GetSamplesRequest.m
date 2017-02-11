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

@end
