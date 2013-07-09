using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Microsoft.Xna.Framework.Graphics;
using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Input;

namespace AlienGirl
{
    class Item
    {
        Rectangle r;
        String owner;
        Texture2D image;
        String name;
        Boolean visible;
        Boolean pass; //if character can pass in front of it or not

        public Item(String what, Texture2D texture, String where, Boolean isPassable)
        {
            name = what;
            image = texture;
            r.Location = new Point(-1, -1);
            r.Height = image.Height;
            r.Width = image.Width;
            owner = where;
            pass = isPassable;
        }
        public Item(String what, Texture2D texture, Point where, Boolean isPassable)
        {
            name = what;
            image = texture;
            r.Location = where;
            r.Height = image.Height;
            r.Width = image.Width;
            owner = null;
            pass = isPassable;
        }

        #region Getters and Setters
        public Texture2D Image
        {
            get { return image; }
            set { image = value; }
        }
        public Boolean Visible
        {
            get { return visible; }
            set { visible = value; }
        }
        public Rectangle CollisionBox
        {
            get { return r; }
            set { r = value; }
        }
        public String Owner
        {
            get { return owner; }
            set { owner = value; }
        }
        public String Name
        {
            get { return name; }
            set { name = value; }
        }
        public Boolean Passable
        {
            get { return pass; }
            set { pass = value; }
        }
        #endregion

        public void Draw(SpriteBatch spriteBatch, Boolean visible)
        {
                if (visible)
                    spriteBatch.Draw(image, r, Color.White);
        }
    }
}
