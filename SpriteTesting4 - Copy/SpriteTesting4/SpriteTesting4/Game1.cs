using System;
using System.Collections.Generic;
using System.Linq;
using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Audio;
using Microsoft.Xna.Framework.Content;
using Microsoft.Xna.Framework.GamerServices;
using Microsoft.Xna.Framework.Graphics;
using Microsoft.Xna.Framework.Input;
using Microsoft.Xna.Framework.Media;

namespace AlienGirl
{
    public class Game1 : Microsoft.Xna.Framework.Game
    {
        GraphicsDeviceManager graphics;
        SpriteBatch spriteBatch;
        SpriteFont font;
        

        #region Textures
        //Texture2D t2dAlien;
        Texture2D t2dGirl;
        Texture2D t2dBall;
        #endregion

        //Dictionary<String, Room> rooms;

        #region Characters
        Character Rosie;
        //Character Rhotrax;
        //Dictionary<String, NPC> npclist;
        #endregion

        #region Items
        Item ball;
        Boolean ballVisible = true;
        #endregion

        public Game1()
        {
            graphics = new GraphicsDeviceManager(this);
            Content.RootDirectory = "Content";
            //this.graphics.IsFullScreen = true;
        }

        /// <summary>
        /// Allows the game to perform any initialization it needs to before starting to run.
        /// This is where it can query for any required services and load any non-graphic
        /// related content.  Calling base.Initialize will enumerate through any components
        /// and initialize them as well.
        /// </summary>
        protected override void Initialize()
        {            
            this.IsMouseVisible = true;
            base.Initialize();
        }

        /// <summary>
        /// LoadContent will be called once per game and is the place to load
        /// all of your content.
        /// </summary>
        protected override void LoadContent()
        {
            // Create a new SpriteBatch, which can be used to draw textures.
            spriteBatch = new SpriteBatch(GraphicsDevice);
            font = Content.Load<SpriteFont>("titleFont");

            t2dGirl = Content.Load<Texture2D>(@"Textures\PrincessCharacter");
            
            t2dBall = Content.Load<Texture2D>(@"Textures\ball");
            ball = new Item("Ball", t2dBall, (new Point(500, 100)), false);


            Rosie = new Character(t2dGirl, "Rosie");
            Rosie.Sprite.AddAnimation("leftstop", 0, 0, 32, 64, 1, 0.1f);
            Rosie.Sprite.AddAnimation("left", 0, 0, 32, 64, 4, 0.1f);
            Rosie.Sprite.AddAnimation("rightstop", 100, 64, 32, 64, 1, 0.1f);
            Rosie.Sprite.AddAnimation("right", 0, 64, 32, 64, 4, 0.1f);
            Rosie.Sprite.CurrentAnimation = "rightstop";
            Rosie.Sprite.AutoRotate = false;
            Rosie.IsCollidable = false;
            Rosie.Position = new Vector2(100, 100);
            Rosie.Target = Rosie.Position;
            Rosie.LoopPath = false;
            Rosie.Speed = 2;
            Rosie.FontColor = Color.Purple;
            
        }

        /// <summary>
        /// UnloadContent will be called once per game and is the place to unload
        /// all content.
        /// </summary>
        protected override void UnloadContent()
        {
            // TODO: Unload any non ContentManager content here
        }

        /// <summary>
        /// Allows the game to run logic such as updating the world,
        /// checking for collisions, gathering input, and playing audio.
        /// </summary>
        /// <param name="gameTime">Provides a snapshot of timing values.</param>
        protected override void Update(GameTime gameTime)
        {
            // Allows the game to exit
            if (GamePad.GetState(PlayerIndex.One).Buttons.Back == ButtonState.Pressed)
                this.Exit();

            MouseState ms = Mouse.GetState();
            Point mousePos = new Point(ms.X, ms.Y);
            KeyboardState ks = Keyboard.GetState();

            if (ks.IsKeyDown(Keys.I))
            {
                //if inventory is no up, put it up

                //if inventory is up, get rid of it
            }

            if (GraphicsDevice.Viewport.Bounds.Contains(mousePos))
            {
                if (ms.LeftButton == ButtonState.Pressed)
                {
                    if (ms.X > Rosie.Position.X)
                    {
                        if (Rosie.Sprite.CurrentAnimation != "right")
                        {
                            Rosie.Sprite.CurrentAnimation = "right";
                        }
                    }
                    else
                    {
                        if (Rosie.Sprite.CurrentAnimation != "left")
                        {
                            Rosie.Sprite.CurrentAnimation = "left";
                        }
                    }
                    Rosie.Target = new Vector2(ms.X - 15, ms.Y - 40);
                    if (ball.CollisionBox.Contains(mousePos) && ballVisible) //And she's nearby
                    {
                        Rosie.Inv.addItem(ball, "Ball");
                        //play animation
                        ballVisible = false; //remove from screen
                    }
                }
                if (Rosie.Position == Rosie.Target)
                {
                    if (Rosie.Sprite.CurrentAnimation == "left")
                    {
                        Rosie.Sprite.CurrentAnimation = "leftstop";
                    }
                    if (Rosie.Sprite.CurrentAnimation == "right")
                    {
                        Rosie.Sprite.CurrentAnimation = "rightstop";
                    }
                }
            }
            Rosie.Update(gameTime);
            base.Update(gameTime);

        }

        /// <summary>
        /// This is called when the game should draw itself.
        /// </summary>
        /// <param name="gameTime">Provides a snapshot of timing values.</param>
        protected override void Draw(GameTime gameTime)
        {
            GraphicsDevice.Clear(Color.CornflowerBlue);

            spriteBatch.Begin();
            Rosie.Draw(spriteBatch);
            ball.Draw(spriteBatch, ballVisible);
            DrawText();
            spriteBatch.End();

            base.Draw(gameTime);
        }

        private void DrawText()
        {
            spriteBatch.DrawString(font, "Cannon power: 100", new Vector2(20, 45), Rosie.FontColor);
        }
    }
}
