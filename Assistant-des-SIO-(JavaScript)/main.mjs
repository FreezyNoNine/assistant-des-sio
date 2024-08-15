import { Client, GatewayIntentBits } from 'discord.js';
import { exec } from 'child_process';

const client = new Client({ intents: [GatewayIntentBits.Guilds] });
const TOKEN = 'coucou toi';

client.on('ready', () => {
  console.log(`Le bot est connecté en tant que : ${client.user.tag}!`);

  // Enregistre les commandes slash ici
  client.guilds.cache.forEach(guild => {
    guild.commands.create({
      name: 'devoirs',
      description: 'Utilise cette commande pour afficher les devoirs à faire.',
      options: [
        {
          name: 'username',
          description: 'Entrez votre pseudo pronote',
          type: 3,
          required: true,
        },
        {
          name: 'password',
          description: 'Entrez votre mot de passe pronote',
          type: 3,
          required: true,
        },
      ],
    });
  });
});

client.on('interactionCreate', async interaction => {
  if (!interaction.isCommand()) return;

  const { commandName, options } = interaction;

  if (commandName === 'devoirs') {
    const username = options.getString('username');
    const password = options.getString('password');

    // Utilise interaction.deferReply() pour différer la réponse
    await interaction.deferReply();

    // Exécute le script Python en passant les arguments
    exec(`python C:\\Users\\XxJib\\OneDrive\\Documents\\Assistant-des-SIO-(Interlangage)\\Assistant-des-SIO-(Python)\\main.py ${username} ${password}`, async (error, stdout, stderr) => {
      if (error) {
        console.error(`Erreur lors de l'exécution du script Python: ${error.message}`);
        return;
      }

      // stdout contient la sortie du script Python
      console.log(`Résultat du script Python: ${stdout}`);

      // Vérifie si stdout est vide
      if (stdout.trim() === '') {
        // Si stdout est vide, envoie un message explicatif
        await interaction.editReply('Aucun devoir trouvé.');
      } else {
        // Si stdout contient du contenu, envoie le message
        await interaction.editReply(`${stdout}`);
      }
    });
  }
});




client.login(TOKEN);


