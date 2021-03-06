//
//  AppDelegate.m
//
//

#import "AppDelegate.h"
#import "PythonistaAppViewController.h"

@implementation AppDelegate

@synthesize window = _window;
@synthesize viewController = _viewController;

- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions 
{	
	_window = [[UIWindow alloc] initWithFrame:[[UIScreen mainScreen] bounds]];
	
	NSString *bundledScriptPath = [[NSBundle mainBundle] pathForResource:@"Script" ofType:@"py"];
	NSString *docPath = [NSSearchPathForDirectoriesInDomains(NSDocumentDirectory, NSUserDomainMask, YES) objectAtIndex:0];
	NSString *targetPath = [docPath stringByAppendingPathComponent:[bundledScriptPath lastPathComponent]];
	
	NSFileManager *fm = [NSFileManager defaultManager];
	NSDictionary *bundledFileAttributes = [fm attributesOfItemAtPath:bundledScriptPath error:NULL];
	NSDictionary *fileAttributes = [fm attributesOfItemAtPath:targetPath error:NULL];
	if (!fileAttributes || ![[bundledFileAttributes fileModificationDate] isEqualToDate:[fileAttributes fileModificationDate]]) {
		[fm removeItemAtPath:targetPath error:NULL];
		[fm copyItemAtPath:bundledScriptPath toPath:targetPath error:NULL];
	}
	
	_viewController = self.viewController = [[[PythonistaAppViewController alloc] initWithScriptPath:targetPath backgroundColor:[UIColor colorWithWhite:0.2 alpha:1.0] textColor:[UIColor colorWithWhite:0.9 alpha:1.0]] autorelease];
	_window.rootViewController = _viewController;
	[_window makeKeyAndVisible];
	return YES;
}

- (void)dealloc
{
	[_viewController release];
	[_window release];
	[super dealloc];
}


@end
