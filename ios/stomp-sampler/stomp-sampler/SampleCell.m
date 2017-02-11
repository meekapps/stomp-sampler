//
//  SampleCell.m
//  stomp-sampler
//
//  Created by Mike Keller on 2/10/17.
//  Copyright © 2017 Perka. All rights reserved.
//

#import "Sample.h"
#import "SampleCell.h"

@interface SampleCell()
@property (weak, nonatomic) IBOutlet UILabel *filenameLabel;
@end

@implementation SampleCell

- (void) awakeFromNib {
  [super awakeFromNib];
}

- (void) setSample:(Sample*)sample {
  self.filenameLabel.text = sample.filename;
}

@end
