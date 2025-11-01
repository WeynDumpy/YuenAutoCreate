import os
import sys
import re
import time
import json
import requests
import random
import string
import hashlib
from bs4 import BeautifulSoup
from faker import Faker
from fake_useragent import UserAgent

# --- Begin: Save helper for Termux (paste after imports) ---
import os
from datetime import datetime

# safe Downloads path that Android file managers show
SAVE_FILE = os.path.expanduser('~/storage/downloads/weynFBCreate.txt')
os.makedirs(os.path.dirname(SAVE_FILE), exist_ok=True)

def save_success_account(uid: srt, password: str= None) -> bool:
    """
    Append a successful account line to SAVE_FILE.
    Format: uid|password|uid|
    """
    try:
        ts = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if uid:
            line = f"{email}|{password}|{uid}|{ts}\n"
        else:
            line = f"{email}|{password}|{ts}\n"
        # append and flush to disk immediately
        with open(SAVE_FILE, 'a', encoding='utf-8') as fh:
            fh.write(line)
            fh.flush()
            try:
                os.fsync(fh.fileno())
            except Exception:
                pass
        # try to make file readable by Android file manager
        try:
            os.chmod(SAVE_FILE, 0o666)
        except Exception:
            pass
        return True
    except Exception as e:
        print(f"[!] save_success_account error: {e}")
        return False
# --- End: Save helper ---


# Enhanced Color codes for terminal with more styling options
class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    DIM = '\033[2m'
    BLINK = '\033[5m'

# Clear screen for better presentation
os.system('clear' if os.name != 'nt' else 'cls')

# Beautiful WEYN banner with purple and blue
print(f"""
{Colors.PURPLE}╔══════════════════════════════════════════════════════════╗
║  {Colors.BLUE}██╗    ██╗{Colors.PURPLE}███████╗{Colors.BLUE}██╗   ██╗{Colors.PURPLE} ███╗   ██╗                {Colors.PURPLE}║
║  {Colors.BLUE}██║    ██║{Colors.PURPLE}██╔════╝{Colors.BLUE}╚██╗ ██╔╝{Colors.PURPLE} ████╗  ██║                {Colors.PURPLE}║
║  {Colors.BLUE}██║ █╗ ██║{Colors.PURPLE}█████╗  {Colors.BLUE} ╚████╔╝ {Colors.PURPLE} ██╔██╗ ██║                {Colors.PURPLE}║
║  {Colors.BLUE}██║███╗██║{Colors.PURPLE}██╔══╝  {Colors.BLUE}  ╚██╔╝  {Colors.PURPLE} ██║╚██╗██║                {Colors.PURPLE}║
║  {Colors.BLUE}╚███╔███╔╝{Colors.PURPLE}███████╗{Colors.BLUE}   ██║   {Colors.PURPLE} ██║ ╚████║                {Colors.PURPLE}║
║  {Colors.BLUE} ╚══╝╚══╝ {Colors.PURPLE}╚══════╝{Colors.BLUE}   ╚═╝   {Colors.PURPLE} ╚═╝  ╚═══╝                {Colors.PURPLE}║
║                                                          ║
║          {Colors.CYAN}FACEBOOK ACCOUNT CREATOR - PRO VERSION{Colors.PURPLE}          ║
║              {Colors.GREEN}BY: WEYN DUMP • PAID TOOL{Colors.PURPLE}                   ║
╚══════════════════════════════════════════════════════════╝{Colors.RESET}
""")
print(f'{Colors.BLUE}{"=" * 60}{Colors.RESET}')

FILIPINO_FIRST_NAMES_MALE = [
    'Juan', 'Jose', 'Miguel', 'Gabriel', 'Rafael', 'Antonio', 'Carlos', 'Luis',
    'Marco', 'Paolo', 'Angelo', 'Joshua', 'Christian', 'Mark', 'John', 'James',
    'Daniel', 'David', 'Michael', 'Jayson', 'Kenneth', 'Ryan', 'Kevin', 'Neil',
    'Jerome', 'Renzo', 'Carlo', 'Andres', 'Felipe', 'Diego', 'Mateo', 'Lucas'
    'Adrian', 'Albert', 'Aldrin', 'Alfred', 'Allen', 'Alonzo', 'Amiel',
    'Andre', 'Andrew', 'Angelo', 'Anton', 'Arden', 'Aries', 'Arman', 'Arnel',
    'Arnold', 'Arthur', 'August', 'Avery', 'Benito', 'Benjamin', 'Bernard',
    'Blake', 'Bryan', 'Bryant', 'Caleb', 'Cameron', 'Cedric', 'Cesar',
    'Charles', 'Christianne', 'Clarence', 'Clark', 'Clint', 'Clyde', 'Colin',
    'Conrad', 'Crispin', 'Cyril', 'Damian', 'Darrel', 'Daryl', 'Darren',
    'Dean', 'Denver', 'Derrick', 'Dexter', 'Dominic', 'Dylan', 'Earl', 'Edgar',
    'Edison', 'Edward', 'Edwin', 'Eli', 'Elias', 'Elijah', 'Emil', 'Emmanuel',
    'Eric', 'Ernest', 'Eron', 'Ethan', 'Eugene', 'Ferdinand', 'Francis',
    'Frank', 'Fred', 'Frederick', 'Galen', 'Garry', 'Genesis', 'Geo', 'Gerald',
    'Gilbert', 'Giovanni', 'Greg', 'Gregory', 'Hans', 'Harold', 'Henry',
    'Hugh', 'Ian', 'Iñigo', 'Irvin', 'Isaac', 'Ivan', 'Jake', 'Jared',
    'Jarred', 'Jason', 'Jasper', 'Jay', 'Jayden', 'Jerald', 'Jericho',
    'Jethro', 'Jimmy', 'Joel', 'Jonas', 'Jonathan', 'Jordan', 'Joseph',
    'Julius', 'Justin', 'Karl', 'Kayden', 'Keith', 'Kelvin', 'Kiel', 'King',
    'Kirk', 'Kyle', 'Lance', 'Larry', 'Lawrence', 'Leandro', 'Leo', 'Leonard',
    'Levi', 'Liam', 'Lorenzo', 'Louie', 'Lucas', 'Lucio', 'Luisito', 'Macario',
    'Malcolm', 'Marcus', 'Mario', 'Martin', 'Marvin', 'Matthew', 'Max',
    'Melvin', 'Mico', 'Miguelito', 'Milan', 'Mitch', 'Nathan', 'Nathaniel',
    'Neilson', 'Nelson', 'Nicholas', 'Nico', 'Noel', 'Norman', 'Oliver',
    'Oscar', 'Owen', 'Patrick', 'Paulo', 'Peter', 'Philip', 'Pierre', 'Ralph',
    'Randall', 'Raymond', 'Reagan', 'Reggie', 'Rein', 'Reiner', 'Ricardo',
    'Rico', 'Riel', 'Robbie', 'Robert', 'Rodney', 'Roldan', 'Romeo', 'Ronald',
    'Rowell', 'Russell', 'Ryanne', 'Sam', 'Samuel', 'Santino', 'Sean', 'Seth',
    'Shawn', 'Simon', 'Stephen', 'Steven', 'Taylor', 'Terrence', 'Theo',
    'Timothy', 'Tomas', 'Tristan', 'Troy', 'Tyler', 'Vernon', 'Victor',
    'Vincent', 'Virgil', 'Warren', 'Wayne', 'Wilfred', 'William', 'Winston',
    'Wyatt', 'Xander', 'Zachary', 'Zion', 'Arvin', 'Dion', 'Harvey', 'Irvin',
    'Jeriel', 'Kennard', 'Levin', 'Randel', 'Ramil', 'Rendon', 'Rome', 'Roven',
    'Silas', 'Tobias', 'Uriel', 'Zandro', 'Axl', 'Brysen', 'Ced', 'Clarkson',
    'Deo', 'Eion', 'Errol', 'Franco', 'Gavin', 'Hansel', 'Isidro', 'Jiro',
    'Kiel', 'Loren', 'Matteo', 'Noelito', 'Omar', 'Paxton', 'Quinn', 'Ramon',
    'Renz', 'Sandy', 'Tyrone', 'Ulrich', 'Vince', 'Wesley', 'Yvan', 'Zed',
    'Alric', 'Brent', 'Caden', 'Dionel', 'Ethaniel', 'Fritz', 'Gerson',
    'Hansley', 'Ivar', 'Jeric', 'Kenzo', 'Lex', 'Morris', 'Nate', 'Orville',
    'Pio', 'Quentin', 'Rydel', 'Sergio', 'Tobit', 'Ulysses', 'Val', 'Wade',
    'Yohan', 'Zyren', 'Adley', 'Cairo', 'Drey', 'Enzo', 'Ferris', 'Gale',
    'Hector', 'Iven', 'Jaycee', 'Kaleb', 'Lyndon', 'Macky', 'Nash', 'Oren',
    'Pierce', 'Quino', 'Rustin', 'Sylvio', 'Tanner', 'Ulian', 'Vaughn',
    'Weston', 'Xeno', 'Yuri', 'Zandro', 'Andro', 'Basil', 'Crisanto', 'Derris',
    'Efrain', 'Florenz', 'Gael', 'Hanz', 'Ismael', 'Jeromey', 'Kielan',
    'Lucian', 'Marlo', 'Nerio', 'Osric', 'Patrik', 'Rion', 'Santino', 'Timo',
    'Vin', 'Wilmer', 'Zaim', 'Zen'
]

FILIPINO_FIRST_NAMES_FEMALE = [
    'Maria', 'Ana', 'Sofia', 'Isabella', 'Gabriela', 'Valentina', 'Camila',
    'Angelica', 'Nicole', 'Michelle', 'Christine', 'Sarah', 'Jessica',
    'Andrea', 'Patricia', 'Jennifer', 'Karen', 'Ashley', 'Jasmine', 'Princess',
    'Angel', 'Joyce', 'Kristine', 'Diane', 'Joanna', 'Carmela', 'Isabel',
    'Lucia', 'Elena'
    'Abigail', 'Adeline', 'Adrienne', 'Agnes', 'Aileen', 'Aira', 'Aiza',
    'Alana', 'Alexa', 'Alexis', 'Alice', 'Allyson', 'Alyssa', 'Amara',
    'Amelia', 'Amirah', 'Anabelle', 'Anastasia', 'Andrea', 'Angela', 'Angelie',
    'Angelyn', 'Anita', 'Annabelle', 'Anne', 'Annie', 'Antoinette', 'April',
    'Ariana', 'Arlene', 'Aubrey', 'Audrey', 'Aurora', 'Ava', 'Bea', 'Bella',
    'Bernadette', 'Bianca', 'Blessy', 'Brianna', 'Bridget', 'Carla', 'Carmel',
    'Cassandra', 'Catherine', 'Cecilia', 'Celeste', 'Charisse', 'Charlene',
    'Charlotte', 'Chelsea', 'Cherry', 'Cheska', 'Clarice', 'Claudia', 'Coleen',
    'Colleen', 'Cristina', 'Cynthia', 'Dahlia', 'Danica', 'Daniela',
    'Danielle', 'Darlene', 'Diana', 'Dominique', 'Donna', 'Dorothy', 'Eden',
    'Elaine', 'Eleanor', 'Elisa', 'Eliza', 'Ella', 'Ellen', 'Eloisa', 'Elsa',
    'Emerald', 'Emily', 'Emma', 'Erica', 'Erin', 'Esme', 'Eunice', 'Faith',
    'Fatima', 'Felice', 'Flor', 'Frances', 'Francesca', 'Genevieve', 'Georgia',
    'Gillian', 'Giselle', 'Glenda', 'Grace', 'Gretchen', 'Gwen', 'Hailey',
    'Hannah', 'Hazel', 'Heather', 'Heidi', 'Helen', 'Helena', 'Hope', 'Iana',
    'Irene', 'Irish', 'Isabelle', 'Ivana', 'Ivory', 'Jacqueline', 'Jamie',
    'Jane', 'Janella', 'Janet', 'Janine', 'Janna', 'Jasmine', 'Jean',
    'Jeanine', 'Jem', 'Jenica', 'Jessa', 'Jillian', 'Joan', 'Joanna', 'Joanne',
    'Jocelyn', 'Jolina', 'Joy', 'Judith', 'Julia', 'Julianne', 'Juliet',
    'Justine', 'Kaila', 'Kaitlyn', 'Karen', 'Karina', 'Kate', 'Katrina',
    'Kayla', 'Keira', 'Kendra', 'Kim', 'Kimberly', 'Krisha', 'Krista',
    'Krystel', 'Kyla', 'Kylie', 'Lara', 'Larissa', 'Laura', 'Lauren', 'Lea',
    'Leanne', 'Lena', 'Leslie', 'Lexi', 'Lianne', 'Liza', 'Lorraine', 'Louisa',
    'Louise', 'Lovely', 'Lucille', 'Luna', 'Lyndsay', 'Lyra', 'Mae', 'Maggie',
    'Maja', 'Mandy', 'Marcia', 'Margaret', 'Marian', 'Mariel', 'Marilyn',
    'Marina', 'Marissa', 'Marites', 'Martha', 'Mary', 'Matilda', 'Maureen',
    'Maxine', 'May', 'Megan', 'Melissa', 'Mia', 'Mika', 'Mikayla', 'Mila',
    'Mira', 'Miranda', 'Mirella', 'Monica', 'Nadia', 'Naomi', 'Natalie',
    'Nathalie', 'Nerissa', 'Nika', 'Nina', 'Nora', 'Norma', 'Olivia',
    'Ophelia', 'Pamela', 'Patricia', 'Paula', 'Pauline', 'Pearl', 'Phoebe',
    'Pia', 'Precious', 'Queenie', 'Quiana', 'Rachelle', 'Rae', 'Rain', 'Raisa',
    'Ramona', 'Raven', 'Reina', 'Rhea', 'Rica', 'Richelle', 'Rina', 'Rochelle',
    'Rosa', 'Rosalie', 'Roseanne', 'Rowena', 'Ruth', 'Sabrina', 'Samantha',
    'Samira', 'Sandra', 'Sara', 'Selene', 'Serena', 'Shaira', 'Shaina',
    'Shanelle', 'Shanika', 'Sharon', 'Sheena', 'Sheila', 'Sherlyn', 'Shiela',
    'Shirley', 'Siena', 'Sierra', 'Sofia', 'Sophia', 'Steffany', 'Stephanie',
    'Summer', 'Susan', 'Suzette', 'Sylvia', 'Tanya', 'Tara', 'Tatiana',
    'Tessa', 'Thea', 'Theresa', 'Trisha', 'Trista', 'Valeria', 'Vanessa',
    'Veronica', 'Vicky', 'Victoria', 'Viel', 'Vina', 'Vivian', 'Wendy',
    'Whitney', 'Yasmin', 'Ysabel', 'Yvette', 'Yvonne', 'Zara', 'Zelda', 'Zia',
    'Zoe', 'Althea', 'Arya', 'Beatriz', 'Czarina', 'Dayanara', 'Elora',
    'Fiona', 'Gianna', 'Helena', 'Indira', 'Janine', 'Kalista', 'Larraine',
    'Maeve', 'Noelle', 'Odessa', 'Patrina', 'Rowan', 'Selina', 'Tahlia', 'Una',
    'Vienna', 'Willow', 'Xandra', 'Yanna', 'Zyra', 'Clarissa', 'Diane',
    'Fritzie', 'Harley', 'Ivette', 'Juliana', 'Karmina', 'Leira', 'Maricel',
    'Nerina', 'Odette', 'Pia', 'Riona', 'Sandy', 'Tanya', 'Vielka', 'Winona',
    'Xyla', 'Ysa', 'Zian', 'Adria', 'Aubriel', 'Celina', 'Devina', 'Emerie',
    'Florence', 'Graciela', 'Hilary', 'Isla', 'Jaira', 'Kelsey', 'Lianne',
    'Maika', 'Nashira', 'Orla', 'Perla', 'Quinley', 'Roxanne', 'Soleil',
    'Therese', 'Ulani', 'Verona', 'Xaviera'
]

FILIPINO_LAST_NAMES = [
    'Reyes', 'Santos', 'Cruz', 'Bautista', 'Garcia', 'Flores', 'Gonzales',
    'Martinez', 'Ramos', 'Mendoza', 'Rivera', 'Torres', 'Fernandez', 'Lopez',
    'Castillo', 'Aquino', 'Villanueva', 'Santiago', 'Dela Cruz', 'Perez',
    'Castro', 'Mercado', 'Domingo', 'Gutierrez', 'Ramirez', 'Valdez',
    'Alvarez', 'Salazar', 'Morales', 'Navarro', 'Abad', 'Abella', 'Abellanosa',
    'Acevedo', 'Aguinaldo', 'Aguilar', 'Alcantara', 'Almonte', 'Alonzo',
    'Altamirano', 'Amador', 'Amparo', 'Ancheta', 'Andrada', 'Angeles',
    'Antonio', 'Aquino', 'Araneta', 'Arceo', 'Arellano', 'Arias', 'Asuncion',
    'Avila', 'Ayala', 'Bagasbas', 'Balagtas', 'Balane', 'Balbuena',
    'Ballesteros', 'Baltazar', 'Banaga', 'Bao', 'Barcenas', 'Baron', 'Basa',
    'Basco', 'Bautista', 'Beltran', 'Benitez', 'Bernal', 'Blanco', 'Borja',
    'Briones', 'Buendia', 'Bustamante', 'Caballero', 'Cabanilla', 'Cabrera',
    'Cadiz', 'Calderon', 'Camacho', 'Canlas', 'Capili', 'Carpio', 'Castañeda',
    'Castroverde', 'Catapang', 'Celis', 'Ceniza', 'Cerda', 'Chavez',
    'Clemente', 'Coloma', 'Concepcion', 'Cordova', 'Cornejo', 'Coronel',
    'Corpuz', 'Cortez', 'Cruzado', 'Cuenca', 'Cuevas', 'Dacanay', 'Daguio',
    'Dalisay', 'Daluz', 'Damaso', 'Dancel', 'Danganan', 'De Guzman',
    'Del Mundo', 'Del Rosario', 'Delos Reyes', 'Deluna', 'Desamparado',
    'Dimaandal', 'Dimaculangan', 'Dizon', 'Dolor', 'Duque', 'Ebarle',
    'Echevarria', 'Elizalde', 'Encarnacion', 'Enriquez', 'Escalante',
    'Escobar', 'Escueta', 'Espinosa', 'Espiritu', 'Estrella', 'Evangelista',
    'Fabian', 'Fajardo', 'Falcon', 'Fernan', 'Ferrolino', 'Ferrer', 'Figueras',
    'Florencio', 'Fonseca', 'Francisco', 'Fuentes', 'Galang', 'Galvez',
    'Garay', 'Garing', 'Gaspar', 'Gavino', 'Giron', 'Godinez', 'Gomez',
    'Gonzaga', 'Granado', 'Guerrero', 'Guevarra', 'Guinto', 'Hernandez',
    'Herrera', 'Hilario', 'Ignacio', 'Ilagan', 'Inocencio', 'Intal', 'Isidro',
    'Jacinto', 'Javier', 'Jimenez', 'Labao', 'Lacson', 'Ladines', 'Lagman',
    'Lao', 'Lara', 'Lasala', 'Lazaro', 'Legaspi', 'Leones', 'Leviste',
    'Liwanag', 'Lorenzo', 'Lucero', 'Lumibao', 'Luna', 'Macaraig', 'Madarang',
    'Madrid', 'Magalong', 'Magbago', 'Magno', 'Magpantay', 'Malabanan',
    'Malig', 'Malinao', 'Manalo', 'Mangahas', 'Mangubat', 'Manlapig', 'Manuel',
    'Marasigan', 'Marquez', 'Martel', 'Matic', 'Melendres', 'Meneses',
    'Miranda', 'Mojica', 'Montero', 'Montoya', 'Morante', 'Moreno', 'Moya',
    'Naval', 'Nieva', 'Nieto', 'Nieves', 'Nolasco', 'Obando', 'Ocampo',
    'Oliva', 'Olivares', 'Ong', 'Ordonez', 'Ortega', 'Ortiz', 'Osorio',
    'Padilla', 'Paguio', 'Palacio', 'Palma', 'Pangan', 'Panganiban',
    'Panlilio', 'Pantoja', 'Paredes', 'Parilla', 'Parungao', 'Pasco', 'Pastor',
    'Patricio', 'Pineda', 'Pizarro', 'Po', 'Policarpio', 'Ponce', 'Quijano',
    'Quimpo', 'Quinto', 'Quirino', 'Rafael', 'Ramoso', 'Razon', 'Redillas',
    'Relucio', 'Remulla', 'Riego', 'Rigor', 'Rivadeneira', 'Rizal', 'Robles',
    'Rocha', 'Rodriguez', 'Rojo', 'Romualdez', 'Rosa', 'Rosales', 'Rosario',
    'Rueda', 'Ruiz', 'Sablan', 'Salas', 'Salcedo', 'Salinas', 'Samson',
    'San Juan', 'San Miguel', 'Sandoval', 'Santillan', 'Santoson', 'Sarmiento',
    'Segovia', 'Sereno', 'Sia', 'Silang', 'Silva', 'Sison', 'Soledad',
    'Soliman', 'Soriano', 'Subido', 'Suarez', 'Sumangil', 'Sy', 'Tablante',
    'Tabora', 'Tacorda', 'Tagle', 'Tamayo', 'Tan', 'Tangonan', 'Tantoco',
    'Tapales', 'Taruc', 'Tejada', 'Tiongson', 'Tolentino', 'Tongco', 'Toribio',
    'Trinidad', 'Tronqued', 'Tuazon', 'Ubaldo', 'Ugalde', 'Umali', 'Untalan',
    'Uy', 'Valencia', 'Valenton', 'Valera', 'Valle', 'Vargas', 'Velasco',
    'Velasquez', 'Vergara', 'Verzosa', 'Villafuerte', 'Villalobos', 'Villamor',
    'Villanueva', 'Villareal', 'Vizcarra', 'Yamamoto', 'Yap', 'Yatco', 'Yumul',
    'Zabala', 'Zamora', 'Zarate', 'Zavalla', 'Zialcita'
]

RPW_NAMES_MALE = [
    'Zephyr', 'Shadow', 'Phantom', 'Blaze', 'Storm', 'Frost', 'Raven', 'Ace',
    'Knight', 'Wolf', 'Dragon', 'Phoenix', 'Thunder', 'Void', 'Eclipse',
    'Nexus', 'Atlas', 'Orion', 'Dante', 'Xavier', 'Axel', 'Kai', 'Ryker',
    'Jax', 'Cole', 'Zane', 'Blake', 'Rex', 'Ash', 'Chase', 'Zero', 'Jet',
    'Aero', 'Aethan', 'Aether', 'Ajax', 'Alaric', 'Alden', 'Alpha', 'Altair',
    'Andros', 'Apollo', 'Arden', 'Aries', 'Arion', 'Arrow', 'Asher', 'Auron',
    'Bane', 'Baron', 'Blaine', 'Blitz', 'Bolt', 'Brax', 'Bren', 'Brody',
    'Cael', 'Cairo', 'Caine', 'Calix', 'Cato', 'Caz', 'Cipher', 'Clade',
    'Corin', 'Crimson', 'Cross', 'Cyric', 'Cyro', 'Daemon', 'Dane', 'Darius',
    'Dash', 'Draco', 'Draven', 'Dren', 'Dusk', 'Echo', 'Eldric', 'Elric',
    'Ember', 'Eon', 'Eryk', 'Exel', 'Ezren', 'Falco', 'Fenix', 'Finn', 'Flare',
    'Flint', 'Fyn', 'Gale', 'Gavin', 'Gideon', 'Grayson', 'Grimm', 'Griff',
    'Halcyon', 'Hale', 'Hawk', 'Helix', 'Hiro', 'Hunter', 'Ignis', 'Indra',
    'Ira', 'Izan', 'Jace', 'Jaden', 'Jairus', 'Jaro', 'Jett', 'Jiro', 'Kael',
    'Kane', 'Kash', 'Kaze', 'Kieran', 'Kian', 'Kiel', 'Knighton', 'Knox',
    'Kross', 'Kyran', 'Lance', 'Lazar', 'Leif', 'Leo', 'Leon', 'Lior', 'Lucan',
    'Luca', 'Luken', 'Lux', 'Lynx', 'Mace', 'Maddox', 'Mael', 'Magnus',
    'Malik', 'Marx', 'Maverick', 'Maxen', 'Milo', 'Nash', 'Nero', 'Nevan',
    'Niall', 'Nico', 'Niko', 'Nyx', 'Odin', 'Onyx', 'Oric', 'Orin', 'Orren',
    'Ozric', 'Pax', 'Phoenixon', 'Quinn', 'Quill', 'Raine', 'Ralph', 'Raze',
    'Rayne', 'Reign', 'Remy', 'Ren', 'Rexxar', 'Rian', 'Riven', 'Rogue',
    'Ronin', 'Rowen', 'Ryder', 'Rylan', 'Sage', 'Sailor', 'Salem', 'Saren',
    'Saxon', 'Seth', 'Shadowen', 'Silas', 'Skye', 'Slate', 'Soren', 'Steel',
    'Sterling', 'Strider', 'Talon', 'Tate', 'Taven', 'Thane', 'Theo', 'Theron',
    'Thorn', 'Tidus', 'Titan', 'Trace', 'Trent', 'Troy', 'Tycho', 'Valen',
    'Valor', 'Vance', 'Varian', 'Vayne', 'Ven', 'Vex', 'Viktor', 'Vin', 'Vyn',
    'Wade', 'War', 'Warden', 'West', 'Wraith', 'Wyatt', 'Wynn', 'Xan',
    'Xander', 'Xenon', 'Xero', 'Xian', 'Yaro', 'Yven', 'Zade', 'Zair', 'Zan',
    'Zander', 'Zayden', 'Zephyrion', 'Zev', 'Zion', 'Zyke', 'Zylo', 'Ares',
    'Auronis', 'Bryn', 'Caelum', 'Corvus', 'Drax', 'Dray', 'Eldan', 'Erykson',
    'Fenrir', 'Gael', 'Hael', 'Ignacio', 'Isen', 'Jareth', 'Kaizen', 'Kyros',
    'Lucius', 'Maelstrom', 'Neroz', 'Obsidian', 'Pyrrus', 'Quen', 'Razeel',
    'Saber', 'Syver', 'Talren', 'Torin', 'Ulric', 'Vael', 'Vairn', 'Wolfe',
    'Xeran', 'Yvain', 'Zypher', 'Azren', 'Bray', 'Crix', 'Drayke', 'Elian',
    'Finnick', 'Gareth', 'Hayen', 'Ivran', 'Joran', 'Kalen', 'Kylen', 'Lioren',
    'Merrick', 'Nairo', 'Orrick', 'Pryce', 'Quor', 'Ronan', 'Sirius', 'Taren',
    'Thornel', 'Ulricon', 'Valik', 'Wendric', 'Xyren', 'Yurei', 'Zeid',
    'Zyric', 'Cyen', 'Auren', 'Bran', 'Caius', 'Darrow', 'Eren', 'Fynric',
    'Grey', 'Hadric', 'Icar', 'Jeran', 'Kairn', 'Lorn', 'Maceon', 'Noctis',
    'Orren', 'Rydan', 'Sylas', 'Taro', 'Vexel', 'Wyren', 'Zen', 'Zyn', 'Axl',
    'Brynn', 'Cyricon', 'Drayven', 'Exar', 'Fen', 'Galen', 'Hex', 'Izen',
    'Jaxen', 'Kyr', 'Lyrik', 'Myrr', 'Nio', 'Onar', 'Pheon', 'Rahn', 'Stryker',
    'Tyr', 'Vorn', 'Wex', 'Xael', 'Ymir', 'Zor', 'Zyricon', 'Ardyn', 'Calren',
    'Delric', 'Eonix', 'Farron', 'Gryx', 'Halren', 'Iven', 'Korr', 'Lyric',
    'Marren', 'Naze', 'Oric', 'Prynn', 'Ryn', 'Sorenix'
]

RPW_NAMES_FEMALE = [
    'Luna', 'Aurora', 'Mystic', 'Crystal', 'Sapphire', 'Scarlet', 'Violet',
    'Rose', 'Athena', 'Venus', 'Nova', 'Stella', 'Serena', 'Raven', 'Jade',
    'Ruby', 'Pearl', 'Ivy', 'Willow', 'Hazel', 'Skye', 'Aria', 'Melody',
    'Harmony', 'Grace', 'Faith', 'Hope', 'Trinity', 'Destiny', 'Serenity',
    'Angel', 'Star', 'Astra', 'Lyra', 'Celeste', 'Elara', 'Elysia', 'Raine',
    'Sylvie', 'Nahara', 'Isolde', 'Ophelia', 'Althea', 'Calista', 'Delara',
    'Eira', 'Freya', 'Gaia', 'Helena', 'Ilara', 'Junia', 'Kaia', 'Liora',
    'Maeve', 'Nara', 'Odessa', 'Phoebe', 'Quinn', 'Rhea', 'Selene', 'Thalia',
    'Una', 'Vanya', 'Wynter', 'Xanthe', 'Yara', 'Zara', 'Amara', 'Aurelia',
    'Brina', 'Celine', 'Dahlia', 'Eden', 'Fiona', 'Gwen', 'Helia', 'Isla',
    'Jessa', 'Kara', 'Lilia', 'Mara', 'Nerine', 'Oona', 'Perse', 'Runa',
    'Sana', 'Tara', 'Vera', 'Willa', 'Xena', 'Yvaine', 'Zinnia', 'Aislinn',
    'Arielle', 'Belladonna', 'Briar', 'Cassia', 'Daphne', 'Eleni', 'Flora',
    'Gemma', 'Hera', 'Ione', 'Jadea', 'Kaira', 'Lilith', 'Maven', 'Nerida',
    'Orla', 'Petra', 'Quilla', 'Risa', 'Saphira', 'Tessa', 'Vixie', 'Wren',
    'Yuna', 'Zelie', 'Aiyana', 'Ameera', 'Blaire', 'Camina', 'Daria', 'Eirene',
    'Faye', 'Greta', 'Honora', 'Indira', 'Jolie', 'Kahlia', 'Lunara', 'Maris',
    'Nixie', 'Oriana', 'Phaedra', 'Reina', 'Soleil', 'Tahlia', 'Viera',
    'Whisper', 'Xylia', 'Yasmin', 'Zephyra', 'Adira', 'Ariya', 'Brienne',
    'Coraline', 'Dove', 'Emberly', 'Fable', 'Giselle', 'Harlow', 'Ivyra',
    'Jorah', 'Keira', 'Lyrra', 'Mirelle', 'Nimue', 'Ophira', 'Paloma', 'Rivka',
    'Sarai', 'Tirzah', 'Velia', 'Wynna', 'Xaria', 'Yllia', 'Zalina', 'Amoura',
    'Aven', 'Brisa', 'Cassidy', 'Diantha', 'Elva', 'Farrah', 'Giada', 'Hollis',
    'Inara', 'Jadeen', 'Kiera', 'Leira', 'Maelle', 'Naida', 'Orra', 'Pyria',
    'Riona', 'Saphine', 'Tova', 'Vanyael', 'Winry', 'Xavia', 'Ysella', 'Zyria',
    'Alera', 'Arwen', 'Brielle', 'Cyrene', 'Deira', 'Evania', 'Fianna',
    'Gwenna', 'Halyn', 'Irina', 'Jovina', 'Kaelia', 'Luneth', 'Mariel',
    'Nayla', 'Orelle', 'Phaena', 'Ruelle', 'Sylph', 'Thessaly', 'Valea',
    'Wynnair', 'Xenara', 'Ysolde', 'Zamira', 'Alira', 'Amaris', 'Brynna',
    'Ceres', 'Delyra', 'Eislyn', 'Fiora', 'Gwyne', 'Haelia', 'Ismena', 'Jalyn',
    'Katria', 'Liorael', 'Maelis', 'Nessara', 'Ovelyn', 'Prisma', 'Ravine',
    'Seraphine', 'Tahlira', 'Vierael', 'Wyndra', 'Xylara', 'Yvanna', 'Zerina',
    'Anora', 'Aveline', 'Brienne', 'Cynra', 'Danea', 'Eirlys', 'Fael', 'Giana',
    'Hessia', 'Ilona', 'Janessa', 'Kyria', 'Lirael', 'Madria', 'Norelle',
    'Ophirae', 'Paela', 'Quina', 'Rilith', 'Sienna', 'Tiriel', 'Velisse',
    'Wrena', 'Xamira', 'Ysenne', 'Zynra', 'Aelina', 'Alessa', 'Belwyn',
    'Carmine', 'Daelia', 'Elyndra', 'Fiorael', 'Gwyneth', 'Helis', 'Isola',
    'Jynra', 'Kailen', 'Lunisse', 'Mynra', 'Nyelle', 'Orissa', 'Phira',
    'Rylis', 'Saphyre', 'Thyra', 'Valyn', 'Wynelle', 'Xira', 'Ylith', 'Zayra',
    'Avenia', 'Ariael', 'Blythe', 'Corra', 'Delyth', 'Elaina', 'Fara', 'Gisra',
    'Hellen', 'Ionea', 'Jalisa', 'Kayle', 'Lysandra', 'Mirael', 'Nysa',
    'Ophirael', 'Phaelia', 'Renelle', 'Saphra', 'Tirra', 'Viona', 'Wynlie',
    'Xynna', 'Ylia', 'Zinnara', 'Azura', 'Bliss', 'Cassiel', 'Dionne',
    'Elaris', 'Fawn', 'Gloria', 'Haelyn', 'Inessa', 'Jael', 'Koryn', 'Lissara',
    'Marenne'
]

RPW_LAST_NAMES = [
    'Shadow', 'Dark', 'Light', 'Star', 'Moon', 'Sun', 'Sky', 'Night', 'Dawn',
    'Storm', 'Frost', 'Fire', 'Stanley', 'Nero', 'Clifford', 'Volsckev',
    'Draven', 'Smith', 'Greisler', 'Wraith', 'Hale', 'Voss', 'Lockhart',
    'Ashford', 'Wynters', 'Grayson', 'Ravenwood', 'Langford', 'Averill',
    'Cross', 'Kane', 'Holloway', 'Mercer', 'Devereux', 'Vale', 'Alden',
    'Blackwell', 'Marcellis', 'Vossler', 'Crane', 'Laurent', 'Radcliffe',
    'Hadrian', 'Vexley', 'Roth', 'Everhart', 'Winslow', 'Fayden', 'Crawford',
    'Ashborne', 'Davenport', 'Drayton', 'Sutherland', 'Vayne', 'Rosenthal',
    'Arkwright', 'Devere', 'Langley', 'Kingsley', 'Vanora', 'Astor',
    'Carrington', 'Trevane', 'Remmington', 'Wolfe', 'Drayke', 'Hawke', 'Briar',
    'Sterling', 'Crowhurst', 'Marlowe', 'Hastings', 'Westwood', 'Ravenshire',
    'Locke', 'Harrow', 'Draxler', 'Valemont', 'Caine', 'Redgrave', 'Frost',
    'Vanthorn', 'Ashcroft', 'Moreau', 'Rothwell', 'Varen', 'Lancaster',
    'Ashfield', 'Sinclair', 'Duskwood', 'Vermillion', 'Whitlock', 'Halden',
    'Faust', 'Ironwood', 'Drayven', 'Grey', 'Valeheart', 'Caldwell', 'Vosslyn',
    'Avenhart', 'Nightray', 'Morraine', 'Leclair', 'Hartgrave', 'Thorne',
    'Montclair', 'Ashen', 'Dreyer', 'Stormwell', 'Vossen', 'Gryphon',
    'Reinhart', 'Claremont', 'Hartley', 'Nightborne', 'Valentine', 'Dreyson',
    'Marchand', 'Blackburn', 'Lucan', 'Callister', 'Hartfield', 'Verden',
    'Draymor', 'Feyr', 'Ravencroft', 'Ainsley', 'Crestfall', 'Silvera',
    'Gravemont', 'Vinter', 'Beaumont', 'Lockridge', 'Thornefield', 'Ashcroft',
    'Crowley', 'Winchester', 'Keller', 'Ravenholm', 'Rosier', 'Everett',
    'Valeon', 'Marrow', 'Vossell', 'Ashenwald', 'Wyncrest', 'Durand',
    'Montague', 'Dreyke', 'Carmine', 'Verlith', 'Harrington', 'Briarson',
    'Corvin', 'Tessler', 'Delane', 'Rayven', 'Fletcher', 'Crosswell',
    'Sterren', 'Valeric', 'Blackthorn', 'Davenport', 'Vanix', 'Dravien',
    'Vexen', 'Rhyker', 'Krynn', 'Greymont', 'Elridge', 'Locksen', 'Harrowell',
    'Valeis', 'Avenor', 'Gravelle', 'Dravenhart', 'Noxford', 'Rothen',
    'Vallier', 'Devereaux', 'Stormvale', 'Kain', 'Drevis', 'Marchen',
    'Langdon', 'Frostell', 'Haldenne', 'Ravenshade', 'Vairn', 'Wyncliff',
    'Greystone', 'Vossmer', 'Ashborne', 'Drexel', 'Rykov', 'Drayven',
    'Malvern', 'Greyhart', 'Holloway', 'Wraithson', 'Crowden', 'Valleris',
    'Stark', 'Wynther', 'Creswell', 'Torrence', 'Arden', 'Fayre', 'Crawell',
    'Thayen', 'Morrick', 'Vanier', 'Drevik', 'Hawthorne', 'Evers', 'Aldric',
    'Larkson', 'Valemir', 'Dravelle', 'Rothenwald', 'Greyvale', 'Veyron',
    'Craven', 'Frostwyn', 'Vares', 'Ashveil', 'Locken', 'Vandrell', 'Silvern',
    'Dawncrest', 'Graves', 'Hartwell', 'Falconer', 'Varnell', 'Ashwynn',
    'Dravenor', 'Vollaire', 'Kingswell', 'Vashier', 'Larkwell', 'Auren',
    'Ravenson', 'Greyborne', 'Voltaire', 'Halewyn', 'Verrin', 'Blackmore',
    'Crimson', 'Wrenford', 'Ravelle', 'Valenor', 'Frostfield', 'Vosswick',
    'Hollowcrest', 'Veyson', 'Atheron', 'Veyra', 'Raines', 'Grimmond',
    'Ashlynn', 'Draywell', 'Vander', 'Vortan', 'Nightwell', 'Vallence', 'Faye',
    'Roswell', 'Stormen', 'Havelock', 'Greys', 'Whitmore', 'Thayne', 'Drevan',
    'Halric', 'Ashmere', 'Westhall', 'Wray', 'Norring', 'Dane', 'Valeir',
    'Kraiven', 'Vosslin', 'Rynhart', 'Eldren', 'Trevane', 'Greisler',
    'Hawthorne', 'Morrin', 'Draylen', 'Aurel', 'Briarson', 'Carter', 'Rexford',
    'Lynhart', 'Ashland', 'Frostwick', 'Vanloren', 'Crowe', 'Vynne',
    'Rothmere', 'Duskhelm', 'Harron', 'Valecrest', 'Merrin', 'Hawken',
    'Dreylor', 'Blackwell', 'Farron', 'Caldren', 'Vanora', 'Hollowen',
    'Varelle', 'Draymore', 'Westcliff', 'Alder', 'Gryff', 'Ashlock', 'Volsen',
    'Drehl', 'Vayden', 'Ravenholt', 'Vossane', 'Krell', 'Marwen', 'Drace',
    'Varenne', 'Lockmere', 'Greysten', 'Hawking', 'Ryswell', 'Drayden',
    'Cresden', 'Hallow', 'Ashven', 'Valter', 'Greyson', 'Morrinell', 'Wraith',
    'Veyden', 'Falken', 'Ashwell'
]


def generate_random_string(length):
    return ''.join(
        random.choices(string.ascii_letters + string.digits, k=length))


def ugenX():
    ua = UserAgent()
    return ua.random


def extractor(data):
    try:
        soup = BeautifulSoup(data, "html.parser")
        result = {}
        for inputs in soup.find_all("input"):
            name = inputs.get("name")
            value = inputs.get("value")
            if name:
                result[name] = value
        return result
    except Exception as e:
        return {"error": str(e)}


def get_filipino_name(gender):
    if gender == '1':
        first_name = random.choice(FILIPINO_FIRST_NAMES_MALE)
    else:
        first_name = random.choice(FILIPINO_FIRST_NAMES_FEMALE)
    last_name = random.choice(FILIPINO_LAST_NAMES)
    return first_name, last_name


def get_rpw_name(gender):
    if gender == '1':
        first_name = random.choice(RPW_NAMES_MALE)
    else:
        first_name = random.choice(RPW_NAMES_FEMALE)
    last_name = random.choice(RPW_LAST_NAMES)
    return first_name, last_name


def generate_password(first_name, last_name):
    name = f"{first_name}{last_name}".replace(' ', '')
    return f"{name}{random.randint(1000, 9999)}"


def generate_temp_email():
    """Generate temporary email using multiple domains to avoid flagging"""
    # Prioritized temp email domains - most reliable first
    domains = [
        # High success rate domains
        'mailto.plus',
        'fexpost.com',
        'fexbox.org',
        'tmpnator.live',
        'laafd.com',
        'dcctb.com',
        'rxcay.com',
        'vusra.com',
        'ezfill.com',
        'civvir.com',
        # Additional backup domains
        'hi2.in',
        'chapedia.net',
        'fextemp.com',
        'upived.com',
        'disbox.org',
        'navalcadets.com',
        'iffymedia.com',
        'edmhdogowsj.com',
        'monadi.ml',
        'laste.ml',
        'fexbox.ru',
        'harakirimail.com',
        'yopmail.com',
        'assurmail.net',
        'cybertemp.xyz',
         'mailinator.com', '10minutemail.com', 'tempmail.net',
    'temp-mail.org', 'guerrillamail.com', 'yopmail.com', 'maildrop.cc',
    'trashmail.com', 'throwawaymail.com', 'mailcatch.com', 'dispostable.com',
    'getnada.com', 'mintemail.com', 'moakt.com', 'spambog.com',
    'mailnesia.com', 'sharklasers.com', 'spamgourmet.com', 'spamfree24.org',
    'easytrashmail.com', 'trashmail.net', 'fakeinbox.com', 'mytemp.email',
    'temp-mail.io', 'emailondeck.com', 'tempinbox.xyz', 'tempmail.live',
    'proxymail.eu', '33mail.com', 'burnermail.io', 'spam4.me',
    'fakemail.net', 'mytrashmail.com'
    ]
    
    # Generate random username with varied length
    username_length = random.randint(10, 15)
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=username_length))
    
    # Select random domain from prioritized list
    domain = random.choice(domains)
    
    return f"{username}@{domain}"


print('\n[+] Select Name Type:')
print('    1. Filipino Names')
print('    2. RPW (Role-Play World) Names')
name_type = input('[?] Enter your choice (1 or 2): ').strip()

if name_type not in ['1', '2']:
    print('[×] Invalid choice! Using Filipino names as default.')
    name_type = '1'

print('\n[+] Select Gender:')
print('    1. Male')
print('    2. Female')
gender_choice = input('[?] Enter your choice (1 or 2): ').strip()

if gender_choice not in ['1', '2']:
    print('[×] Invalid choice! Using Male as default.')
    gender_choice = '1'

fb_gender = "2" if gender_choice == "1" else "1"

print('\n[+] Password Option:')
print('    1. Auto-generated Password (Name + 4 digits)')
print('    2. Custom Password')
password_choice = input('[?] Enter your choice (1 or 2): ').strip()

custom_password = None
if password_choice == '2':
    custom_password = input('[?] Enter your custom password: ').strip()
    if not custom_password:
        print('[×] Empty password! Using auto-generated instead.')
        password_choice = '1'

num_accounts = int(input('\n[+] How many accounts do you want to create: '))

print(f'\n{Colors.CYAN}[+] Creating {num_accounts} accounts...{Colors.RESET}\n')
print(f'{Colors.BLUE}{"=" * 60}{Colors.RESET}')

oks = []
cps = []

# Progress statistics
start_time = time.time()
print(f'{Colors.CYAN}[⚡] TURBO MODE: Instant account creation enabled!{Colors.RESET}\n')

for i in range(num_accounts):
    try:
            ses = requests.Session()

            response = ses.get(
                url='https://x.facebook.com/reg',
                params={
                    "_rdc": "1",
                    "_rdr": "",
                    "wtsid": "rdr_0t3qOXoIHbMS6isLw",
                    "refsrc": "deprecated"
                },
            )

            mts = ses.get("https://x.facebook.com").text
            m_ts_match = re.search(r'name="m_ts" value="(.*?)"', str(mts))
            m_ts = m_ts_match.group(1) if m_ts_match else ""

            formula = extractor(response.text)

            # Generate email using multiple domains to avoid flagging
            email = generate_temp_email()

            if name_type == '1':
                first_name, last_name = get_filipino_name(gender_choice)
            else:
                first_name, last_name = get_rpw_name(gender_choice)

            if password_choice == '1':
                password = generate_password(first_name, last_name)
            else:
                password = custom_password

            birthday_day = str(random.randint(1, 28))
            birthday_month = str(random.randint(1, 12))
            birthday_year = str(random.randint(1990, 2003))

            print(f'[{i+1}] Creating account...')
            print(f'    Name: {first_name} {last_name}')
            print(f'    Email: {Colors.BLUE}{email}{Colors.RESET}')
            print(f'    Password: {password}')
            

            payload = {
            'ccp': "2",
            'reg_instance': str(formula.get("reg_instance", "")),
            'submission_request': "true",
            'helper': "",
            'reg_impression_id': str(formula.get("reg_impression_id", "")),
            'ns': "1",
            'zero_header_af_client': "",
            'app_id': "103",
            'logger_id': str(formula.get("logger_id", "")),
            'field_names[0]': "firstname",
            'firstname': first_name,
            'lastname': last_name,
            'field_names[1]': "birthday_wrapper",
            'birthday_day': birthday_day,
            'birthday_month': birthday_month,
            'birthday_year': birthday_year,
            'age_step_input': "",
            'did_use_age': "false",
            'field_names[2]': "reg_email__",
            'reg_email__': email,
            'field_names[3]': "sex",
            'sex': fb_gender,
            'preferred_pronoun': "",
            'custom_gender': "",
            'field_names[4]': "reg_passwd__",
            'name_suggest_elig': "false",
            'was_shown_name_suggestions': "false",
            'did_use_suggested_name': "false",
            'use_custom_gender': "false",
            'guid': "",
            'pre_form_step': "",
            'encpass': f'#PWD_BROWSER:0:{int(time.time())}:{password}',
            'submit': "Sign Up",
            'm_ts': m_ts,
            'fb_dtsg': str(formula.get("fb_dtsg", "")),
            'jazoest': str(formula.get("jazoest", "")),
            'lsd': str(formula.get("lsd", "")),
            '__dyn': str(formula.get("__dyn", "")),
            '__csr': str(formula.get("__csr", "")),
            '__req': str(formula.get("__req", "p")),
            '__fmt': str(formula.get("__fmt", "1")),
            '__a': str(formula.get("__a", "")),
            '__user': "0"
            }

            header1 = {
            "Host": "m.facebook.com",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": ugenX(),
            "Accept":
            "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "dnt": "1",
            "X-Requested-With": "mark.via.gp",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-User": "?1",
            "Sec-Fetch-Dest": "document",
            "dpr": "1.75",
            "viewport-width": "980",
            "sec-ch-ua":
            '"Android WebView";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            "sec-ch-ua-mobile": "?1",
            "sec-ch-ua-platform": '"Android"',
            "sec-ch-prefers-color-scheme": "dark",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
            }

            reg_url = "https://www.facebook.com/reg/submit/?privacy_mutation_token=eyJ0eXBlIjowLCJjcmVhdGlvbl90aW1lIjoxNzM0NDE0OTk2LCJjYWxsc2l0ZV9pZCI6OTA3OTI0NDAyOTQ4MDU4fQ%3D%3D&multi_step_form=1&skip_suma=0&shouldForceMTouch=1"

            py_submit = ses.post(reg_url,
                                 data=payload,
                                 headers=header1,
                                 timeout=30)

            if "c_user" in py_submit.cookies:
                first_cok = ses.cookies.get_dict()
                uid = str(first_cok["c_user"])

                # Success with enhanced display
                print(f'    {Colors.GREEN}{Colors.BOLD}✓ SUCCESS!{Colors.RESET} Account created instantly')
                print(f'    {Colors.DIM}Email:{Colors.RESET} {Colors.CYAN}{email}{Colors.RESET}')
                print(f'    {Colors.DIM}User ID:{Colors.RESET} {Colors.YELLOW}{uid}{Colors.RESET}')
                print(f'    {Colors.DIM}Status:{Colors.RESET} {Colors.GREEN}Active (No verification needed){Colors.RESET}')

                # Save to weynFBCreate.txt file
               with open('/data/data/com.termux/files/home/storage/downloads/weynFBCreate.txt', 'a') as f:
                    f.write(
                        f"{uid}| {password} | \n" )
                  print("[✅] Account Saved Successfully!")
except Exception as e:
    print(f"[❌] Save Error: {e}")
                oks.append(uid)

                print(f'{Colors.BLUE}{"─" * 60}{Colors.RESET}')
                
            else:
                print(f'    {Colors.RED}✗ FAILED!{Colors.RESET} Account creation failed')
                print(f'    {Colors.DIM}Email may be flagged or rate limited{Colors.RESET}')
                cps.append(email)
                print(f'{Colors.BLUE}{"─" * 60}{Colors.RESET}')

    except Exception as e:
        print(f'    {Colors.RED}✗ ERROR!{Colors.RESET} {str(e)[:100]}')
        cps.append('error')
        print(f'{Colors.BLUE}{"─" * 60}{Colors.RESET}')

# Calculate statistics
end_time = time.time()
elapsed_time = end_time - start_time
accounts_per_sec = len(oks) / elapsed_time if elapsed_time > 0 else 0
success_rate = (len(oks) / num_accounts * 100) if num_accounts > 0 else 0

print(f'\n{Colors.BLUE}{"=" * 60}{Colors.RESET}')
print(f'{Colors.PURPLE}{Colors.BOLD}╔═══════════════════════════════════════════╗{Colors.RESET}')
print(f'{Colors.PURPLE}{Colors.BOLD}║        ⚡ CREATION SUMMARY ⚡              ║{Colors.RESET}')
print(f'{Colors.PURPLE}{Colors.BOLD}╚═══════════════════════════════════════════╝{Colors.RESET}\n')

print(f'{Colors.WHITE}{Colors.BOLD}📊 Statistics:{Colors.RESET}')
print(f'   {Colors.DIM}Total Attempts:{Colors.RESET} {Colors.CYAN}{num_accounts}{Colors.RESET}')
print(f'   {Colors.GREEN}✓ Successful:{Colors.RESET}  {Colors.GREEN}{Colors.BOLD}{len(oks)}{Colors.RESET} {Colors.GREEN}({success_rate:.1f}%){Colors.RESET}')
print(f'   {Colors.RED}✗ Failed:{Colors.RESET}      {Colors.RED}{len(cps)}{Colors.RESET}')
print(f'   {Colors.YELLOW}⚡ Speed:{Colors.RESET}       {Colors.YELLOW}{accounts_per_sec:.2f} accounts/sec{Colors.RESET}')
print(f'   {Colors.CYAN}⏱️ Time:{Colors.RESET}        {Colors.CYAN}{elapsed_time:.2f} seconds{Colors.RESET}')

if len(oks) > 0:
    print(f'\n{Colors.GREEN}{Colors.BOLD}💾 File Saved:{Colors.RESET}')
    print(f'   {Colors.DIM}Filename:{Colors.RESET} {Colors.CYAN}weynFBCreate.txt{Colors.RESET}')
    print(f'   {Colors.DIM}Location:{Colors.RESET} {Colors.DIM}{os.path.abspath("weynFBCreate.txt")}{Colors.RESET}')
    print(f'   {Colors.DIM}Total Accounts:{Colors.RESET} {Colors.GREEN}{len(oks)}{Colors.RESET}')
    
    print(f'\n{Colors.PURPLE}{Colors.BOLD}📥 DOWNLOAD INSTRUCTIONS:{Colors.RESET}')
    print(f'   {Colors.CYAN}① Left sidebar → Find "weynFBCreate.txt"{Colors.RESET}')
    print(f'   {Colors.CYAN}② Right-click → Download{Colors.RESET}')
    print(f'   {Colors.CYAN}③ Open with any text editor{Colors.RESET}')
else:
    print(f'\n{Colors.YELLOW}{Colors.BOLD}⚠️  No successful accounts created{Colors.RESET}')
    print(f'   {Colors.DIM}Try again or check your internet connection{Colors.RESET}')

print(f'\n{Colors.BLUE}{"=" * 60}{Colors.RESET}')
print(f'{Colors.PURPLE}{Colors.BOLD}Thank you for using WEYN FB Creator Pro! {Colors.RESET}')
print(f'{Colors.BLUE}{"=" * 60}{Colors.RESET}\n')
