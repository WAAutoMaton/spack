% Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
% Spack Project Developers. See the top-level COPYRIGHT file for details.
%
% SPDX-License-Identifier: (Apache-2.0 OR MIT)

%=============================================================================
% Avoid cycles in the DAG
%
% Some combinations of conditional dependencies can result in cycles;
% this ensures that we solve around them. Note that these rules are quite
% demanding on both grounding and solving, since they need to compute and
% consider all possible paths between pair of nodes.
%=============================================================================


#program no_cycle.
path(Parent, Child) :- depends_on(Parent, Child).
path(Parent, Descendant) :- path(Parent, A), depends_on(A, Descendant).
:- path(A, A).

#defined depends_on/2.
