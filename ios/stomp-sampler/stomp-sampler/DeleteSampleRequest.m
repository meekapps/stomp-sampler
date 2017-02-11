//
//  DeleteSampleRequest.m
//  stomp-sampler
//
//  Created by Mike Keller on 2/11/17.
//  Copyright © 2017 Perka. All rights reserved.
//

#import "DeleteSampleRequest.h"

@implementation DeleteSampleRequest

- (instancetype) initWithSample:(NSString*)sample {
  NSString *path = [NSString stringWithFormat:@"/sample/%@", sample];
  self = [super initWithMethod:HttpMethodDelete
                          path:path];
  if (self) {}
  return self;
}

@end
