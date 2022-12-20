#include <stdio.h>
#include <unistd.h>

typedef struct{

} grass_t;

typedef struct{

}sun_t;

typedef struct{
  int limit;
} frog_t;

typedef struct{

} tree_t;

typedef struct{
    frog_t frog;
    grass_t grass;
    sun_t sun;
    tree_t tree;
} world_t;

void frog_construct(world_t*, const int*);
void have_air(const int, const int);
void isLight(const int, const int);
void frogIsEating(const int, const int, const int);
void frogIsAwake(const int, const int);
void run(int*, const int, const int limit);
void world_construct(world_t*, sun_t*, tree_t*, frog_t*, grass_t*);

int main(){
    int start = 0;
    int seconds;
    int limit;

    world_t world;
    tree_t tree;
    grass_t grass;
    sun_t sun;
    frog_t frog;
    
    world_construct(&world, &sun, &tree, &frog, &grass);
    printf("%s", "How many hours is your day have?\n");
    scanf("%d", &seconds);
    printf("%s", "Enter limit of frogs eating with count.\n");
    scanf("%d", &limit);
    frog_construct(&world, &limit);
    printf("%d", world.frog.limit);
    run(&start, seconds, limit);
}

void world_construct(world_t* world,sun_t* sun, tree_t* tree, frog_t* frog, grass_t* grass){
    world->frog = *frog;
    world->sun = *sun;
    world->tree = *tree;
    world->grass = *grass;
}

void frog_construct(world_t* world, const int* limit){
     world->frog.limit = *limit;
}

void have_air(const int start, const int seconds){
    if(start <= (seconds / 2)){
        printf("%s", "The tree produces oxygen.");
    }
    else{
        printf("%s", "The tree not produces oxygen.");
    }
}

void isLight(const int start, const int seconds){
    if(start <= (seconds / 2)){
        printf("%s", "The sun is shining.");
    }
    else{
        printf("%s", "The sun is not shining.");
    }
}

void frogIsEating(const int start, const int seconds, const int limit){
    if(start <= (seconds / 2) && start <= limit){
        printf("%s", "Frog is eating.\n");
    }
    else{
        printf("%s",  "Frog is not eating.\n");
    }
}   

void frogIsAwake(const int start, const int seconds){
    if(start <= (seconds / 2)){
        printf("%s", "Frog is awake.");
    }
    else{
        printf("%s", "Frog is sleeping.");
    }
}

void run(int* start, const int seconds, const int limit){
    while(*start != seconds){
    usleep(1000000);
    (*start)++;
    isLight(*start, seconds);
    have_air(*start, seconds);
    frogIsAwake(*start, seconds);
    frogIsEating(*start, seconds, limit);
    }
    *start = 0;
    run(start, seconds, limit);
}