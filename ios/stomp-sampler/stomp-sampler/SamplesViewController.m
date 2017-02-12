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
  self = [super initWithNibName:NSStringFromClass([self class])
                         bundle:[NSBundle mainBundle]];
  if (self) {
  }
  return self;
}

- (void) viewDidLoad {
  [super viewDidLoad];
  
  [self setupPullToRefresh];
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

- (UITableViewCellEditingStyle) tableView:(UITableView *)tableView
            editingStyleForRowAtIndexPath:(NSIndexPath *)indexPath {
  return UITableViewCellEditingStyleDelete;
}

- (void) tableView:(UITableView *)tableView
commitEditingStyle:(UITableViewCellEditingStyle)editingStyle
 forRowAtIndexPath:(NSIndexPath *)indexPath {
  [self deleteSampleAtIndexPath:indexPath];
}

- (UITableViewCell*) tableView:(UITableView *)tableView cellForRowAtIndexPath:(NSIndexPath *)indexPath {
  SampleCell *cell = [(SamplesTableView*)tableView dequeueCell];
  cell.sample = self.samples[indexPath.row];
  return cell;
}

#pragma mark - Private

- (void) deleteSampleAtIndexPath:(NSIndexPath*)indexPath {
  Sample *sample = self.samples[indexPath.row];
  
  __weak typeof(self) weakSelf = self;
  [[Api deleteSampleRequestWithSample:sample.filename] executeWithCompletion:^(NSArray<Sample *> *samples) {
    weakSelf.samples = samples;
    [weakSelf.tableView beginUpdates];
    [weakSelf.tableView deleteRowsAtIndexPaths:@[indexPath] withRowAnimation:UITableViewRowAnimationAutomatic];
    [weakSelf.tableView endUpdates];
  }];
}

- (void) refreshSamples {
  __weak typeof(self) weakSelf = self;
  [[Api getSamplesRequest] executeWithCompletion:^(NSArray<Sample *> *samples) {
    [weakSelf.tableView.refreshControl endRefreshing];
    weakSelf.samples = samples;
    [weakSelf.tableView reloadData];
  }];
}

- (void) setupPullToRefresh {
  UIRefreshControl *refresh = [[UIRefreshControl alloc] init];
  [refresh addTarget:self
              action:@selector(refreshSamples)
    forControlEvents:UIControlEventPrimaryActionTriggered];
  self.tableView.refreshControl = refresh;
}

@end
