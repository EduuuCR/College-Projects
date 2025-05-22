import models.Member;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

public class MemberTest {

    @Test
    public void testMemberCreation() {
        Member member = new Member("Jane Doe");
        assertEquals("Jane Doe", member.getName());
    }

    @Test
    public void testToString() {
        Member member = new Member("John Doe");
        assertTrue(member.toString().contains("John Doe"));
    }
}
