# Game engine - HW2

## Introduction

Connect 4 (also known as Four Up, Plot Four, Find Four, Captain's Mistress, Four in a Row, Drop Four, and Gravitrips) is a two-player connection board game, in which the players choose a color and then take turns dropping colored tokens into a seven-column, six-row vertically suspended grid. The pieces fall straight down, occupying the lowest available space within the column. The objective of the game is to be the first to form a horizontal, vertical, or diagonal line of four of one's own tokens. Connect Four is a solved game. The first player can always win by playing the right moves.

You can visit https://www.youtube.com/watch?v=utXzIFEVPjA to learn more about connect 4 game.

## Description

In this homework, you'll be implementing Minimax and Alpha-Beta Pruning for an agent playing connect 4. Wait, isn't Alpha-Beta Pruning a variant of Minimax? Yes, it is. It's just that here we're using Minimax and Alpha-Beta Pruning to respectively refer to Minimax WITHOUT Alpha-Beta Pruning and Minimax WITH Alpha-Beta Pruning.

But first, you should get practically familiar with how the game is played, not just be familiar with the rules of the game. To do this, play the game with the provided code by running environemnt.py. You've been distributed a codebase which includes an interface for playing the game in a variety of modes. Notably, you don't need to actually make the game of Connect 4 —just make an agent that plays it.

Playing the game interactively and is tested on Linux and Mac. However, this is not required for completing the assignment and is only provided to help you get familiar with the game (and for your entertainment).

## What you need to do: 

***
Now that you know how the game is played, it is time to make your own intelligent players of the game. You will do this my implementing one player that use Minimax and another player that uses Alpha-Beta Pruning.

### Minimax

Minimax is an algorithm for determing the best move in an adverserial game. It seeks to minimize the maximum loss posed by the opponent’s strategy. Minimax is typically employed in competitive, discrete-, and finite-space games with abstracted time and perfect information. You will complete the implementation of minimax in student_code.py

### Minimax with Alpha-Beta Pruning

You may notice that Minimax starts to get terribly slow when you set your maximum search depth to values above, say, 4. This makes perfect sense when you think about the fact that the total number of nodes in your game tree is the branching factor to the power of the search depth. For comparatively "bushy" games (e.g., chess, Go, etc.) the branching factor is prohibitively large, which is why agents that play these games use cleverer algorithms to choose what move to take next.

One such cleverer algorithm (although still not clever enough to do well at games like Go) is a modification of Minimax known as Alpha-Beta Pruning. They are, at their core, the same algorithm. The distinction is that A-B Pruning ignores subtrees that are provably worse than any that it has considered so far. This drastically reduces the runtime of the algorithm. Since A-B Pruning is a variant of Minimax, you aren't really writing a new algorithm; rather, you're taking your implementation of Minimax and making it a little smarter.

Strictly speaking, it doesn't change the upper bound on the algorithm's runtime, since in the worst-case one must still search the entire tree. In practice, however, the performance difference is very noticeable.

As with Minimax, your task is to complete the implementation of minimaxAlphaBeta.

## What is expected : 

***
*You need to complete the code blocks in minimax and minimaxAlphaBeta
*Run student_code.py and check if the AI is able to play game against you successfully
*Report your moves and AI moves you tested with

