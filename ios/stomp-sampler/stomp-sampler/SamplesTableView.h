//
//  SamplesTableView.h
//  stomp-sampler
//
//  Created by Mike Keller on 2/10/17.
//  Copyright © 2017 Perka. All rights reserved.
//

@import UIKit;

@class SampleCell;

@interface SamplesTableView : UITableView

- (SampleCell*) dequeueCell;

@end
