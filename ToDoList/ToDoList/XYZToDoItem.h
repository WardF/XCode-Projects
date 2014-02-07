//
//  XYZToDoItem.h
//  ToDoList
//
//  Created by Ward Fisher on 2/7/14.
//  Copyright (c) 2014 Ward Fisher. All rights reserved.
//

#import <Foundation/Foundation.h>

@interface XYZToDoItem : NSObject

@property NSString *itemName;
@property BOOL completed;
@property (readonly) NSDate *creationDate;

@end
