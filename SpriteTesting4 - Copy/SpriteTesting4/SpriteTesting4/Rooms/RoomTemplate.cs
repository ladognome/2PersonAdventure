using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Microsoft.Xna.Framework.Graphics;
using Microsoft.Xna.Framework;

namespace AlienGirl
{
    class Room
    {
        String name;
        Texture background;
        Dictionary<String, Item> items;
        Dictionary<String, Rectangle> exits;
        Dictionary<String, NPC> NPCs;
        Boolean girlPresent;
        Boolean alienPresent;

    }
}
