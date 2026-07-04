// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 78;

// Hash table
node *table[N];

int loaded_words = 0;

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    int index = hash(word);
    node *tmp = table[index];

    while (tmp != NULL)
    {
        if (strcasecmp(tmp->word, word) == 0)
        {
            return true;
        }

        tmp = tmp->next;
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    int index = 0;

    for (int i = 0, n = strlen(word); i < n; i++)
    {
        index += tolower(word[i]);
    }

    if (index > (N - 1))
    {
        index %= N;
    }

    return index;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    FILE *source = fopen(dictionary, "r");
    if (source == NULL)
    {
        printf("Can't open file\n");
        return false;
    }

    char word[LENGTH + 1];

    while (fscanf(source, "%45s", word) == 1)
    {
        node *new_node = malloc(sizeof(node));
        if (new_node == NULL)
        {
            printf("Error\n");
            unload();
            fclose(source);
            return false;
        }

        strcpy(new_node->word, word);

        int index = hash(word);
        new_node->next = table[index];
        table[index] = new_node;

        loaded_words++;
    }

    fclose(source);

    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return loaded_words;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    for (unsigned int i = 0; i < N; i++)
    {
        node *current = table[i];

        while (current != NULL)
        {
            node *tmp = current->next;
            free(current);
            current = tmp;
        }
    }
    return true;
}
