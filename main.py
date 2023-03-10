from model.organisation import Organisation
from model.person import Person


def main() -> None:
    org = Organisation()

    alice = Person("alice", expertise=[0.1, 0.0, 0.9])
    bob = Person("bob", expertise=[0.5, 0.3, 0.4])

    alice.join(org)
    x = alice.work([0.4, 0.4, 0.2])
    print(x)

    for m in org._members:
        print(m.name)


if __name__ == '__main__':
    main()