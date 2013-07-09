using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Microsoft.Xna.Framework.Graphics;
using Microsoft.Xna.Framework;

namespace AlienGirl
{
    class Inventory //TODO: make this draggable
    {
        public Dictionary<String, Item> list;
        private int numOfCols;
        private int numOfSlots;


        public Inventory()
        {
            list = new Dictionary<String, Item>();
            numOfCols = 0;
            numOfSlots = 0;
        }

        public Dictionary<String, Item> List
        {
            get { return list; }
            set {list = value;}
        }

        public Inventory(Dictionary<String, Item> startingInv, int cols, int slots)
        {
            list = startingInv;
            numOfCols = cols;
            numOfSlots = slots;
        }

        public void addItem(Item i, String whohas)
        {
            if (!list.ContainsKey(i.Name))
            {
                if (i != null)
                {
                    list.Add(i.Name, i);
                    i.Owner = whohas;
                }
            }
        }
        public void removeItem(Item i)
        {
            if (list.ContainsKey(i.Name))
            {
                list.Remove(i.Name);
                i.Owner = null;
            }
        }
        public Item getItem(string itemName)
        {
            if (list.ContainsKey(itemName))
            {
                Item item = list[itemName];
                return item;
            }
            return null;
            
            
        }

        public void Draw(SpriteBatch spriteBatch, int XOffset, int YOffset)
        {
                /*spriteBatch.Draw(t2dTexture, (v2Position + new Vector2(XOffset, YOffset) + v2Center),
                                CurrentFrameAnimation.FrameRectangle, colorTint,
                                fRotation, v2Center, 1f, SpriteEffects.None, 0);*/
        }
    }
}
