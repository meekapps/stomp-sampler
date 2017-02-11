//
//  Sample.h
//  stomp-sampler
//
//  Created by Mike Keller on 2/10/17.
//  Copyright © 2017 Perka. All rights reserved.
//

@import UIKit;

@interface Sample : NSObject

@property (copy, nonatomic, readonly) NSString *filename;

- (instancetype) initWithFilename:(NSString*)filename;

@end
