//
//  Api.m
//  stomp-sampler
//
//  Created by Mike Keller on 2/10/17.
//  Copyright © 2017 Perka. All rights reserved.
//

#import "Api.h"

@implementation Api

+ (GetSamplesRequest*) getSamplesRequest {
  GetSamplesRequest *request = [[GetSamplesRequest alloc] init];
  return request;
}

+ (DeleteSampleRequest*) deleteSampleRequestWithSample:(NSString*)sample {
  DeleteSampleRequest *request = [[DeleteSampleRequest alloc] initWithSample:sample];
  return request;
}

@end
