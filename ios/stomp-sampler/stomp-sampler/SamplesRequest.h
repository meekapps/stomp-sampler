//
//  SamplesRequest.h
//  stomp-sampler
//
//  Created by Mike Keller on 2/11/17.
//  Copyright © 2017 Perka. All rights reserved.
//

#import "ApiRequest.h"

@class Sample;

typedef void(^SamplesCompletion)(NSArray <Sample*>*samples);

@interface SamplesRequest : ApiRequest <ApiRequestProtocol>

- (void) executeWithCompletion:(SamplesCompletion)completion;

@end
