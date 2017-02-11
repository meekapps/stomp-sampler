//
//  GetSamplesRequest.h
//  stomp-sampler
//
//  Created by Mike Keller on 2/10/17.
//  Copyright © 2017 Perka. All rights reserved.
//

#import "ApiRequest.h"

@class Sample;

typedef void(^GetSamplesCompletion)(NSArray <Sample*>*samples);

@interface GetSamplesRequest : ApiRequest <ApiRequestProtocol>

- (void) executeWithCompletion:(GetSamplesCompletion)completion;

@end
