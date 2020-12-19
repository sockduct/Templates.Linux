/*
 * James Small
 * SDEV-###-##, <Season> Semester <Year>
 * Week # Assignment
 * Date:  x #, 2020
 * Problem #
 * Version:  2020-11-7-02
 *
 * <PROGRAM NAME>
 * - <FEATURES>
 * 
 * Helpful References:
 * - Modern C (General C Resource):
 *   https://modernc.gforge.inria.fr/
 * - The Linux Programming Interface (Systems Programming):
 *   https://learning.oreilly.com/library/view/the-linux-programming/9781593272203/
 */

#include <errno.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Prototypes:
void exiterr(const char *syscallfn);
int handlerr(int status, const char *syscallfn);
void printerr(const char *syscallfn);

int main(int argc, char *argv[]) {

    return 0;
}

// Note:  Don't pass in errno since it's a global.  Not sure if this could
//        be problematic with multi-threaded code...
void exiterr(const char *syscallfn) {
    printf("Error:  %s errno %d - %s.\n", syscallfn, errno, strerror(errno));

    exit(1);
}

int handlerr(int status, const char *syscallfn) {
    // May want other ways to check for error condition
    // Error conditions:
    // 1) Return code == -1 (typically indicates error)
    //    Exception:  Return code of -1 for getpriority not an error
    // 2) In some cases (e.g., getpriority) must set errno to 0 before call
    //    and check it for non-zero value after call return
    //
    // Note:  This routine currently only deals with case 1
    if (status == -1) {
        printf("Error:  %s errno %d - %s.\n", syscallfn, errno, strerror(errno));

        exit(1);
    } else if (status < -1) {
        printf("Warning:  %s returned negative status of %d, errno currently %d"
               " - %s", syscallfn, status, errno, strerror(errno));
    }

    // Reset errno:
    errno = 0;

    return status;
}

void printerr(const char *syscallfn) {
    printf("Error:  %s errno %d - %s.\n", syscallfn, errno, strerror(errno));

    // Reset errno:
    errno = 0;
}
