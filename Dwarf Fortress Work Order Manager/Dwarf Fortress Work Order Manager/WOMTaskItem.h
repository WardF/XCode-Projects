//
//  WOMTaskItem.h
//  Dwarf Fortress Work Order Manager
//
//  Created by Ward Fisher on 2/12/14.
//  Copyright (c) 2014 Ward Fisher. All rights reserved.
//

#import <Foundation/Foundation.h>

@interface WOMTaskItem : NSObject

-(WOMTaskItem *)initWithValues: (NSString*) task
                         count: (int) c;




@property NSString *taskName;
@property BOOL completed;
@property int m_count; //!< Number of times the task must be completed.
@property int m_complete; //!< Total number of times the task has been completed.



@property NSMutableArray *m_depends; //!< List of tasks that need to be completed first.
@property NSMutableArray *m_enables; //!< List of tasks that are enabled when this task is completed.

@end
