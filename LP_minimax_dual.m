%We do not need to add negative signs to coefficients here because we want
%to minimize
Q = [1 7 5 4 2
    8 3 6 5 1
    3 4 4 9 5
    2 4 11 4 6
    5 3 4 7 12
    ];

b = [1 1 1 1 1];
Q = [Q -b.']
b = b-b
Qeq = [1 1 1 1 1 0]
beq = [1]
f = [0 0 0 0 0 1]
lb = [0 0 0 0 0]

%Solve
[x_, fval_] = linprog(f, Q, b, Qeq, beq, lb)

%Output:

% Optimal solution found.
% 
% 
% x_ =
% 
%     0.3385
%     0.5692
%          0
%          0
%     0.0923
%     4.5077
% 
% 
% fval_ =
% 
%     4.5077

%Here we solved v, so -v (payoff for P2) = -4.5077
%Maxminimizer strategy = x = (0.3385, 0.5692, 0, 0, 0.0923)