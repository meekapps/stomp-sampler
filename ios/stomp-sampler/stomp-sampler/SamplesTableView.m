//
//  SamplesTableView.m
//  stomp-sampler
//
//  Created by Mike Keller on 2/10/17.
//  Copyright © 2017 Perka. All rights reserved.
//

#import "SamplesTableView.h"
#import "SampleCell.h"

@implementation SamplesTableView

- (instancetype) initWithCoder:(NSCoder *)aDecoder {
  self = [super initWithCoder:aDecoder];
  if (self) {
    NSString *cellId = NSStringFromClass([SampleCell class]);
    [self registerNib:[UINib nibWithNibName:cellId
                                     bundle:[NSBundle mainBundle]]
forCellReuseIdentifier:cellId];
    
    self.rowHeight = UITableViewAutomaticDimension;
    self.showsVerticalScrollIndicator = NO;
  }
  return self;
}

- (SampleCell*) dequeueCell {
  return [self dequeueReusableCellWithIdentifier:NSStringFromClass([SampleCell class])];
}

@end
