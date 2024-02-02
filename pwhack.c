#include <stdio.h>
#include <time.h>
#include <unistd.h>
#include <string.h>
#include <stdlib.h>


/* Global variables */
char *password;
char *crackPassword;
int matchFound = 0;

/* Swap values at two pointers */
void swap(char *p1, char *p2) {
    char temp;
    temp = *p1;
    *p1 = *p2;
    *p2 = temp;
}

/* Print permutations of string */
void permute(char *str, int l, int r) {

    int index = 0;

    if (matchFound) {
        return;
    }
   
    if(l == r) {

        printf("\nMatching: %s...", str);

        FILE *fp = fopen("list.txt", "a");
        fputs(str, fp);
        fputc('\n', fp);
        fclose(fp);

        // Locate index of the permuted crackPassword
        /*
        while (crackPassword[index] != '\0') {

            printf("Index: %d \tPosition: %c\n", index, crackPassword[index]);
            index++;
        }
        */
    }

    // Print results when the password has a match
    if (strcmp(password, str) == 0) {

        printf("\n\n\tCOMPLETE\n________________________\n");
        printf("Password: \t%s \nMatch found: \t%s\n", password, str);
        matchFound = 1;
        return;
    } else {

        for(index = l; index <= r; index++) {

            swap((str + l), (str + index));
            permute(str, l + 1, r);
            swap((str + l), (str + index)); // backtrack

        }
    }
}

/* Driver Program */
int main(char argc, char** argv) {
	
    // For early testing, request password to check against permutation
    printf("Password: ");
    password = argv[1];

    

    // Request characters to guess password
    // I would like to have any time a character is found the program will
    // change the permutation process to disclude the found character
    printf("\nMatching Sequence: ");
    crackPassword = argv[2];
    //printf(crackPassword);
    printf("\n");
    int n = strlen(crackPassword);

    // Clock variables and start time
    clock_t t;
    t = clock();
    clock_t begin = clock();

    // Execute permutation function
    permute(crackPassword, 0, n-1);

    // End clock time and print results
    clock_t end = clock();
    double time_taken = (double)(end - begin) / CLOCKS_PER_SEC;
    printf("\nTime: %f\n", time_taken);

    // If password match is not identified, print unsuccessful
    if (matchFound == 0) {
        printf("Unsuccessful...\n");
    }
    return 0;
}
