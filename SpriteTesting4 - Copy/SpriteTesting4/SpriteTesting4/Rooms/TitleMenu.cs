using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Microsoft.Xna.Framework.Graphics;
using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Input;

namespace AlienGirl
{
    public class StartScreen
    {
        private Texture2D texture;
        private Game1 game;
        private KeyboardState lastKState;
        private MouseState lastMState;


        public StartScreen(Game1 game)
        {
            this.game = game;
            texture = game.Content.Load<Texture2D>("StartScreen");
            lastKState = Keyboard.GetState();
            lastMState = Mouse.GetState();
        }

        public void Draw(SpriteBatch spriteBatch, SpriteFont font)
        {
            spriteBatch.DrawString(font, "AlienGirl", new Vector2(50, 50), Color.RosyBrown);
        }
    }
}
