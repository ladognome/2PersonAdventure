using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace AlienGirl
{
    class DialogueTree
    {
        String talkingTo;
        String Initiator;
        

        public DialogueTree(String to, String from)
        {
            talkingTo = to;
            Initiator = from;
            //get the specific conversation's head node and display it
            //based off of what the player chooses, bring up the next group
        }

        //public ConversationLine NextNode()
    }
}
