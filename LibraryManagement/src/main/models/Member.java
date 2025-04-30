package models;

public class Member {
    private String name;

    public Member() {} // Required for JSON serialization

    public Member(String name) {
        this.name = name;
    }

    public String getName() { return name; }

    @Override
    public String toString() {
        return "Member: " + name;
    }
}
