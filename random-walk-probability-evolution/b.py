import random
import matplotlib.pyplot as plt


def rg():
    return random.choice([1, -1])


def sequence(N):
    x = []

    for i in range(N):
        x.append(rg())

    return x


def paths(NP, N):
    y = []

    for i in range(NP):
        x = sequence(N)
        y.append(x)

    return y


def path_sum(path, N):
    s = 0

    for i in range(N):
        s += path[i]

    return s


def P(X, N, path, NP):
    count = 0

    for i in range(NP):

        if X == path_sum(path[i], N):
            count += 1

    return count / NP


def Pi(X, Y, N, M, NP, path):

    count = 0
    total = 0

    for i in range(NP):

        p = path[i].copy()

        # Convert steps into positions
        for j in range(1, N):
            p[j] += p[j - 1]

        if Y == p[M - 1]:

            total += 1

            if X == p[N - 1]:
                count += 1

    if total == 0:
        return 0

    return count / total


def main():

    NP = int(input("Enter No. of Experiments: "))
    X = int(input("Enter X: "))
    N = int(input("Enter N: "))

    # One-step equation
    M = N - 1

    print()
    print("N =", N)
    print("M =", M)


    # =====================================================
    # GENERATE PATHS
    # =====================================================

    path = paths(NP, N)


    # =====================================================
    # LHS
    # =====================================================

    LHS = P(
        X,
        N,
        path,
        NP
    )


    # =====================================================
    # RHS
    # =====================================================

    Pi1 = Pi(
        X,
        X - 1,
        N,
        M,
        NP,
        path
    )

    Pi2 = Pi(
        X,
        X + 1,
        N,
        M,
        NP,
        path
    )

    P1 = P(
        X - 1,
        M,
        path,
        NP
    )

    P2 = P(
        X + 1,
        M,
        path,
        NP
    )

    RHS = (
        Pi1 * P1
    ) + (
        Pi2 * P2
    )


    print()
    print("Pi(X, X-1) =", Pi1)
    print("Pi(X, X+1) =", Pi2)

    print()

    print("P(X-1, M) =", P1)
    print("P(X+1, M) =", P2)

    print()

    print("LHS =", LHS)
    print("RHS =", RHS)

    print()

    print("|LHS - RHS| =", abs(LHS - RHS))


    # =====================================================
    # GRAPH 1
    # RANDOM WALK PATHS
    # =====================================================

    plt.figure(figsize=(10, 6))

    # Plot maximum 100 paths
    for i in range(min(NP, 100)):

        p = path[i].copy()

        for j in range(1, N):
            p[j] += p[j - 1]

        positions = [0] + p

        plt.plot(
            range(N + 1),
            positions
        )

    plt.xlabel("Time Step")
    plt.ylabel("Position")

    plt.title("Random Walk Paths")

    plt.grid(True)

    plt.show()


    # =====================================================
    # GRAPH 2
    # FINAL POSITION DISTRIBUTION
    # =====================================================

    x_values = []
    probability = []

    # Possible positions are
    # -N, -N+2, ..., N-2, N

    for x1 in range(-N, N + 1, 2):

        x_values.append(x1)

        probability.append(
            P(
                x1,
                N,
                path,
                NP
            )
        )


    plt.figure(figsize=(10, 6))

    plt.bar(
        x_values,
        probability,
        width=1.5
    )

    plt.xlabel("Final Position X")
    plt.ylabel("P(S_N = X)")

    plt.title("Distribution of Final Positions")

    plt.grid(
        axis="y"
    )

    plt.show()


    # =====================================================
    # GRAPH 3
    # LHS VS RHS BAR GRAPH
    # =====================================================

    NP_values = [
        100,
        1000,
        10000
    ]

    lhs = []
    rhs = []


    for NP1 in NP_values:

        # Generate new paths
        path1 = paths(
            NP1,
            N
        )


        # LHS

        lhs1 = P(
            X,
            N,
            path1,
            NP1
        )


        # RHS

        rhs1 = (
            Pi(
                X,
                X - 1,
                N,
                M,
                NP1,
                path1
            )
            *
            P(
                X - 1,
                M,
                path1,
                NP1
            )
        ) + (
            Pi(
                X,
                X + 1,
                N,
                M,
                NP1,
                path1
            )
            *
            P(
                X + 1,
                M,
                path1,
                NP1
            )
        )


        lhs.append(lhs1)
        rhs.append(rhs1)


        print()
        print("-------------------------")
        print("NP =", NP1)
        print("LHS =", lhs1)
        print("RHS =", rhs1)
        print(
            "Error =",
            abs(lhs1 - rhs1)
        )


    # Bar graph

    plt.figure(figsize=(10, 6))

    width = 0.35

    x = range(len(NP_values))

    x1 = []
    x2 = []

    for i in x:

        x1.append(i - width / 2)
        x2.append(i + width / 2)


    plt.bar(
        x1,
        lhs,
        width=width,
        label="LHS"
    )

    plt.bar(
        x2,
        rhs,
        width=width,
        label="RHS"
    )


    plt.xticks(
        x,
        NP_values
    )

    plt.xlabel(
        "Number of Experiments (NP)"
    )

    plt.ylabel(
        "Probability"
    )

    plt.title(
        "LHS vs RHS"
    )

    plt.legend()

    plt.grid(
        axis="y"
    )

    plt.show()


if __name__ == "__main__":
    main()