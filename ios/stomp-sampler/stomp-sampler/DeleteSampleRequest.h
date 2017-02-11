//
//  DeleteSampleRequest.h
//  stomp-sampler
//
//  Created by Mike Keller on 2/11/17.
//  Copyright © 2017 Perka. All rights reserved.
//

#import "SamplesRequest.h"

@interface DeleteSampleRequest : SamplesRequest

- (instancetype) initWithSample:(NSString*)sample;

@end
