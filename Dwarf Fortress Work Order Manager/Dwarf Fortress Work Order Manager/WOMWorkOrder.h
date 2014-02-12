//
//  WOMWorkOrder.h
//  Dwarf Fortress Work Order Manager
//
//  Created by Ward Fisher on 2/12/14.
//  Copyright (c) 2014 Ward Fisher. All rights reserved.
//

#import <Foundation/Foundation.h>

@interface WOMWorkOrder : NSObject

@property NSString *name;
@property NSMutableArray *tasks;
@property BOOL completed;

@end
