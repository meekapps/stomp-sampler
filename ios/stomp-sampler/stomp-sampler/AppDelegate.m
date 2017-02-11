//
//  AppDelegate.m
//  stomp-sampler
//
//  Created by Mike Keller on 2/10/17.
//  Copyright © 2017 Perka. All rights reserved.
//

#import "AppDelegate.h"
#import "SamplesViewController.h"

@interface AppDelegate ()
@end

@implementation AppDelegate

- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  self.window = [[UIWindow alloc] initWithFrame:[UIScreen mainScreen].bounds];
  SamplesViewController *samples = [[SamplesViewController alloc] init];
  
  UINavigationController *navigation = [[UINavigationController alloc] initWithRootViewController:samples];
  
  self.window.rootViewController = navigation;
  [self.window makeKeyAndVisible];
  
  return YES;
}

@end
