#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int compare(const void *a, const void *b) {
    return (*(int*)a - *(int*)b);
}

int main() {
    FILE *file = fopen("input.txt", "r");
    if (file == NULL) {
        perror("Error opening file");
        return EXIT_FAILURE;
    }

    int total = 0;

    char *token;
    char *line = NULL;
    size_t len = 0;

    int left[1024] = {0};
    int right[1024] = {0};

    for (int i = 0; getline(&line, &len, file) != -1; i++) {
        token = strtok(line, " ");
        left[i] = atoi(token);
        token = strtok(NULL, " ");
        right[i] = atoi(token);
    }

    int n = sizeof(left) / sizeof(left[0]);

    qsort(left, n, sizeof(int), compare);
    qsort(right, n, sizeof(int), compare);

    for (int i = 0; i < n; i++) {
        total += abs(left[i] - right[i]);
    }

    printf("%d\n", total);

    free(line);
    fclose(file);
    return 0;
}
