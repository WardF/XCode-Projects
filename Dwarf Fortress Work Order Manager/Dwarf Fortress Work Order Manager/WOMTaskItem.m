//
//  WOMTaskItem.m
//  Dwarf Fortress Work Order Manager
//
//  Represents an individual Task
//
//  Created by Ward Fisher on 2/12/14.
//  Copyright (c) 2014 Ward Fisher. All rights reserved.
//

#import "WOMTaskItem.h"

@implementation WOMTaskItem

/*! Initialize with values.
 * 
 &*
 *
 */
-(WOMTaskItem*) initWithValues: (NSString*) task count: (int) c; {
    
    self = [super init];
    if (self) {
        self.taskName = task;
        self.m_count = c;
        self.m_complete = 0;
        self.completed = NO;
    }
    
    return self;
}

@end
