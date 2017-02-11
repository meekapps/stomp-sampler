//
//  ViewController.m
//  stomp-sampler
//
//  Created by Mike Keller on 2/10/17.
//  Copyright © 2017 Perka. All rights reserved.
//

#import "Api.h"
#import "Sample.h"
#import "SampleCell.h"
#import "SamplesTableView.h"
#import "SamplesViewController.h"

@interface SamplesViewController () <UITableViewDataSource, UITableViewDelegate>
@property (strong, nonatomic) UIRefreshControl *refresh;
@property (strong, nonatomic) NSArray <Sample*>*samples;
@property (weak, nonatomic) IBOutlet SamplesTableView *tableView;
@end

@implementation SamplesViewController

- (instancetype) init {
  self = [super initWithNibName:NSStringFromClass([self class]) bundle:[NSBundle mainBundle]];
  if (self) {
  }
  return self;
}

- (void) viewDidLoad {
  [super viewDidLoad];
  
  UIRefreshControl *refresh = [[UIRefreshControl alloc] init];
  [refresh addTarget:self
                   action:@selector(refreshSamples)
         forControlEvents:UIControlEventPrimaryActionTriggered];
  self.tableView.refreshControl = refresh;
}

- (void) viewDidAppear:(BOOL)animated {
  [super viewDidAppear:animated];
  
  [self refreshSamples];
}

#pragma mark - UITableViewDataSource

- (NSInteger) numberOfSectionsInTableView:(UITableView *)tableView {
  return 1;
}

- (NSInteger) tableView:(UITableView *)tableView numberOfRowsInSection:(NSInteger)section {
  return self.samples.count;
}

- (UITableViewCell*) tableView:(UITableView *)tableView cellForRowAtIndexPath:(NSIndexPath *)indexPath {
  SampleCell *cell = [(SamplesTableView*)tableView dequeueCell];
  cell.sample = self.samples[indexPath.row];
  return cell;
}

#pragma mark - Private

- (void) refreshSamples {
  __weak typeof(self) weakSelf = self;
  [[Api getSamplesRequest] executeWithCompletion:^(NSArray<Sample *> *samples) {
    [weakSelf.tableView.refreshControl endRefreshing];
    weakSelf.samples = samples;
    [weakSelf.tableView reloadData];
  }];
}

@end
