using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace AlienGirl
{
    class ConversationLine
    {
        String whoSaidIt;
        String whatIsSaid; //check this
        Boolean saidAlready;
        List<String> alternatives;
        List<ConversationLine> next;
        ConversationLine parent;

        public ConversationLine(String who, String what, List<String> alts, List<ConversationLine> Next, ConversationLine Parent)
        {
            whoSaidIt = who;
            whatIsSaid = what;
            alternatives = alts;
            saidAlready = false;
            next = Next;
            parent = Parent;
        }

        public String RandomAlternative
        {
            get
            {
                Random rng = new Random();
                int n = alternatives.Count;
                while (n > 1)
                {
                    n--;
                    int k = rng.Next(n + 1);
                    String value = alternatives[k];
                    alternatives[k] = alternatives[n];
                    alternatives[n] = value;
                }
                return alternatives.First();
            }
        }
        public String Who
        {
            get { return whoSaidIt; }
            set { whoSaidIt = value; }
        }
        public String What
        {
            get { return whatIsSaid; }
            set { whatIsSaid = value; }
        }
        public List<String> Alternatives
        {
            get { return alternatives; }
            set { alternatives = value; }
        }
        public List<ConversationLine> Next
        {
            get { return next; }
            set { next = value; }
        }
        public ConversationLine Parent
        {
            get { return parent; }
            set { parent = value; }
        }
        public Boolean WasSaid
        {
            get { return saidAlready; }
            set { saidAlready = value; }
        }
    }
}
