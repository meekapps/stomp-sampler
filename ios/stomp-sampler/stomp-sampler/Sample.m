//
//  Sample.m
//  stomp-sampler
//
//  Created by Mike Keller on 2/10/17.
//  Copyright © 2017 Perka. All rights reserved.
//

#import "Sample.h"

@interface Sample()
@property (copy, nonatomic, readwrite) NSString *filename;
@end

@implementation Sample

- (instancetype) initWithFilename:(NSString*)filename {
  self = [super init];
  if (self) {
    self.filename = filename;
  }
  return self;
}

@end
