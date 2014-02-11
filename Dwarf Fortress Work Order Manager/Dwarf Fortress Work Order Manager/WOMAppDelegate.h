//
//  WOMAppDelegate.h
//  Dwarf Fortress Work Order Manager
//
//  Created by Ward Fisher on 2/11/14.
//  Copyright (c) 2014 Ward Fisher. All rights reserved.
//

#import <UIKit/UIKit.h>

@interface WOMAppDelegate : UIResponder <UIApplicationDelegate>

@property (strong, nonatomic) UIWindow *window;

@property (readonly, strong, nonatomic) NSManagedObjectContext *managedObjectContext;
@property (readonly, strong, nonatomic) NSManagedObjectModel *managedObjectModel;
@property (readonly, strong, nonatomic) NSPersistentStoreCoordinator *persistentStoreCoordinator;

- (void)saveContext;
- (NSURL *)applicationDocumentsDirectory;

@end
