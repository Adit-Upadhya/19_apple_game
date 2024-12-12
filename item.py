# Ｅ－４６最初）各種インポート処理
import pygame
import random

# Ｅ－４７）落下物クラス
class Item:

    # Ｅ－４８）コンストラクタ
    def __init__(self, no):
        # Ｅ－４９）アイテムNoをインスタンスの変数に設定
        self.no = no
        # Ｅ－５０）アイテム番号に対応した画像を読み込み
        if self.no == 2:
            self.image = pygame.image.load('image/goldapple.png')
        elif self.no == 3:
            self.image = pygame.image.load('image/hog.png')
        elif self.no == 4:
            self.image = pygame.image.load('image/rock.png')
        else:
            self.image = pygame.image.load('image/apple.png')
        
        
        # Ｆ－６０最初）画像の四角形を取得
        rect = self.image.get_rect()
        # Ｆ－６１）画面上の位置のＸ方向の初期値はランダム
        self.pos_x = random.randint(0, 800 - rect.width)
        # Ｆ－６２）画面上の位置のＹ方向の初期値は画面の少し上
        self.pos_y = 0 - rect.height

    # Ｅ－５１）画面への描画処理
    def draw(self, surface):
        # Ｅ－５２mainへ）一旦固定の位置に描画する
        # Ｆ－６３）アイテムを位置に合わせて描画する
        surface.blit(self.image, (self.pos_x, self.pos_y))  
        
    # Ｆ－６４）落下処理
    def fall(self):
        # Ｆ－６５）金のリンゴと岩は、スピードを速くする
        if self.no == 2 or self.no == 4:
            self.pos_y += 3
        # Ｆ－６６）リンゴとハリネズミは通常速度
        else:
            self.pos_y += 2
        
    # Ｈ－７６mainから）プレイヤーとの当たり判定処理
    def hit_check(self, player_pos_x, player_pos_y, player_width, player_height):
        # Ｈ－７７）アイテムの四角形
        item_rect = self.image.get_rect()
        # Ｈ－７８）アイテムの右端がプレイヤーの左端より左なら、当たっていない
        if self.pos_x + item_rect.width < player_pos_x:
            return 0
        # Ｈ－７９）アイテムの左端がプレイヤーの右端より右なら、当たっていない
        if self.pos_x > player_pos_x + player_width: 
            return 0
        # Ｈ－８０）アイテムの下端がプレイヤーの上端より上なら、当たっていない
        if self.pos_y + item_rect.height < player_pos_y:
            return 0    
        # Ｈ－８１）アイテムの上端がプレイヤーの下端より下なら、当たっていない
        if self.pos_y > player_pos_y + player_height:
            return 0
        # Ｈ－８２playerへ）どれにも当てはまらなければ、当たっている
        print('Hit!', self.no)
        # Ｉ－８９最初）当たった場合は、そのアイテムを画面の下に移動
        self.pos_y = 800
        # Ｉ－９０playerへ）当たったアイテムの番号を戻り値にする
        return self.no 
    
