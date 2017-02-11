//
//  Api.h
//  stomp-sampler
//
//  Created by Mike Keller on 2/10/17.
//  Copyright © 2017 Perka. All rights reserved.
//

#import "GetSamplesRequest.h"
#import "DeleteSampleRequest.h"

@import Foundation;

@interface Api : NSObject

+ (GetSamplesRequest*) getSamplesRequest;
+ (DeleteSampleRequest*) deleteSampleRequestWithSample:(NSString*)sample;

@end
