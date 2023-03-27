from components import consumable
from components.ai import HostileEnemy
from components.fighter import Fighter
from components.inventory import Inventory
from components.level import Level
from entity import Actor, Item

player = Actor(
    char="@",
    color=(255, 255, 255),
    name="Player",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=30, defense=2, power=5),
    inventory=Inventory(capacity=26),
    level=Level(level_up_base=200),
    description=f"It's you!"
)

zorc = Actor(
    char="z",
    color=(63, 127, 63),
    name="Zorc",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=10, defense=0, power=3),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=35),
    description="A little green monster"
)
groll = Actor(
    char="G",
    color=(0, 127, 0),
    name="Groll",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=16, defense=1, power=4),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=100),
    description="A big green monster"
)

confusion_scroll = Item(
    char="~",
    color=(207, 63, 255),
    name="Confusion Scroll",
    consumable=consumable.ConfusionConsumable(number_of_turns=10),
    description="A magical scroll that confuses target enemy"
)

fireball_scroll = Item(
    char="~",
    color=(255, 0, 0),
    name="Fireball Scroll",
    consumable=consumable.FireballDamageConsumable(damage=12, radius=3),
    description="A magical scroll that causes a large explosion around target visible tile"
)

health_potion = Item(
    char="!",
    color=(127, 0, 255),
    name="Health Potion",
    consumable=consumable.HealingConsumable(amount=4),
    description="A healing potion that restores 4 health"
)

orenugget = Item(
    char="*",
    color=(250, 121, 33),
    name="Nugget",
    consumable=consumable.HealingConsumable(amount=1),# TODO: Remove this
    description="A nugget of... wait. It's a chicken nugget."
)

lightning_scroll = Item(
    char="~",
    color=(255, 255, 0),
    name="Lightning Scroll",
    consumable=consumable.LightningDamageConsumable(damage=20, maximum_range=5),
    description="A magical scroll that causes lightning to strike the closest enemy"
)
