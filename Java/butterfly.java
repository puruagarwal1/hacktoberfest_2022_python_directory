public class butterfly {
    public static void main(String[] args) {
        for(int i=1;i<5;i++)
        {
            for(int a=1;a<=i;a++)
            {
                System.out.print("* ");
            }
            int l=8-(2*i);
            for(int b=l;b>0;b--)
            {
                System.out.print("  ");
            }
            for(int a=1;a<=i;a++)
            {
                System.out.print("* ");
            }
            System.out.println();
        }
        for(int i=4;i>0;i--)
        {
            for(int a=1;a<=i;a++)
            {
                System.out.print("* ");
            }
            int l=8-(2*i);
            for(int b=l;b>0;b--)
            {
                System.out.print("  ");
            }
            for(int a=1;a<=i;a++)
            {
                System.out.print("* ");
            }
            System.out.println();
        }
    }
}
