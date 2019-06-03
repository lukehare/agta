%Solving initial LP for minimax value, v, and for the minimaximizer strategy for
%P1, x:

%A equal to coefficients in LP
A = [1 8 3 2 5
    7 3 4 4 3
    5 6 4 11 4
    4 5 9 4 7
    2 1 5 6 12
    ];

%Set A to negative, as we solve LP by maximizing v - (x.T)A
A = -A

b = [1 1 1 1 1];

%Add column of -1s for -v, negative because linprog solves <= rather than
%>=
A = [A -b.']

%Set b to zero 1s have been added to A
b = b-b

%Equality constraints for prob distribution
Aeq = [1 1 1 1 1 0]

%Aeq sums to 1
beq = [1]

%Objective function (set equal to v)
f = [0 0 0 0 0 1]

%lower bound for xis
lb = [0 0 0 0 0]

%Solve
[x, fval] = linprog(f, A, b, Aeq, beq, lb)

%Output:
% Optimal solution found.
% 
% 
% x =
% 
%     0.3769
%     0.3385
%          0
%          0
%     0.2846
%    -4.5077
% 
% 
% fval =
% 
%    -4.5077

%Note: we solved for -v, so v=4.5077
%Minmaximizer strategy = (0.3769, 0.3385, 0, 0, 0.2846)