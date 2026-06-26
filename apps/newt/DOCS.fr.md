### Extension Home Assistant : Documentation
## Client Newt pour le tunnel de proxy inverse Pangolin

Le [système Fossorial – avec Pangolin](https://docs.fossorial.io/) comme composant central – est un proxy inverse tunnelisé auto-hébergé avec gestion des identités et des accès, conçu pour mettre à disposition des ressources privées en toute sécurité via des tunnels WireGuard chiffrés dans l’espace utilisateur. Imaginez cela comme des tunnels Cloudflare auto-hébergés.

Newt est le client principal qui se connecte à Pangolin et permet d’accéder aux services situés sur le même réseau que Newt. Installez-le et connectez-vous à votre instance Pangolin pour permettre l’accès à distance à Home Assistant via des tunnels WireGuard sécurisés.

## Installation

1. Ouvrez Home Assistant.
2. Allez dans **Paramètres → Extensions → Boutique d’extensions → ⋮ → Référentiels**.
3. Ajoutez le référentiel.
4. Installez l’extension **Newt**.
5. Configurez les options de l’extension.
6. Lancez l’extension.

Autorisez Newt à accéder au socket Docker. **Vous devez désactiver le « mode de protection » sur la page principale de l’extension.**

## Home Assistant en tant que ressource...

1. Accédez à votre tableau de bord Pangolin et ajoutez une nouvelle ressource nommée `Home Assistant`. Sélectionnez le site correspondant à l’instance Home Assistant Newt que vous avez définie dans les prérequis, puis attribuez un sous-domaine à votre ressource.
2. Assurez-vous que l’option « Activer SSL » est cochée afin d’obtenir un certificat SSL généré automatiquement pour le chiffrement des connexions du navigateur.
3. Dans la section « Configuration de la cible », ajoutez une cible avec la méthode `HTTP`, le domaine `homeassistant.local.hass.io` et le port `8123`. Cliquez sur « Ajouter une cible » et enregistrez les paramètres.
5. Rendez-vous sur la [documentation de Home Assistant](https://www.home-assistant.io/integrations/http) et suivez les instructions pour ajouter un `trusted_proxy` à votre fichier `configuration.yaml`. Celui-ci est probablement `172.30.33.0/24`. Assurez-vous également de définir `use_x_forwarded_for: true` afin que l’adresse IP du client apparaisse dans vos journaux, et non celle du proxy inverse. Redémarrez Home Assistant.
7. (Facultatif) Si vous souhaitez créer une ressource faisant référence à un add-on Home Assistant, utilisez le slug de l’add-on dans la section « domain » ou dans la zone « Target configuration ». Vous le trouverez sur la page de configuration de l’add-on dans Home Assistant. Dans cet exemple, le slug est « a0d7b954_tailscale ». Si un caractère `_` est présent, comme dans cet exemple, il doit être remplacé par un `-`. Le domaine correct pour cet exemple serait donc `a0d7b954-tailscale`. Votre port dépend de l’add-on ; vous devez consulter la documentation ou la configuration de l’add-on.

## Configuration

| Option | Champ obligatoire | Description |
|---|---|---|
| `endpoint` | ✅ | URL de votre serveur Pangolin, par exemple `https://app.pangolin.net` |
| `id` | ✅ | ID Newt issu du tableau de bord Pangolin |
| `secret` | ✅ | Clé secrète Newt issue du tableau de bord Pangolin |
| `log_level` | ❌ | Niveau de journalisation : `trace`, `debug`, `info`, `warn`, `error` (par défaut : `info`) |
| `docker_socket` | ❌ | Chemin d'accès au socket Docker pour l'extraction des étiquettes, par exemple `/var/run/docker.sock` – voir [la documentation](https://docs.pangolin.net/manage/sites/configure-site#docker-socket-integration) |
| `docker_enforce_network_validation` | ❌ | Forcer la validation du réseau Docker (par défaut : `false`) |
| `dns` | ❌ | Serveur DNS pour la résolution du point de terminaison. (Par défaut : `9.9.9.9`) |
| `disable_clients` | ❌ | Désactiver les clients sur l'interface WireGuard. (Par défaut : `false`) |
| `disable_ssh` | ❌ | Désactiver les démons d'authentification SSH et le mode SSH natif (par défaut : `false`) |
| `no_cloud` | ❌ | Impossible de basculer vers le cloud si vous utilisez des nœuds gérés dans Pangolin Cloud (par défaut : `false`) |
| `ping_interval` | ❌ | Intervalle entre les pings envoyés au serveur (par défaut : `15s`) |
| `ping_timeout` | ❌ | Délai d'expiration pour chaque ping (par défaut : `7s`) |
| `tls_client_cert_file` | ❌ | Chemin d'accès au fichier de certificat client (format PEM/DER) pour mTLS |
| `tls_client_key` | ❌ | Chemin d'accès au fichier de clé privée du client (format PEM/DER) pour mTLS |
| `tls_client_ca` | ❌ | Chemin d'accès au fichier de certificat CA pour la validation des certificats distants (peut être spécifié plusieurs fois) |
| `udp_proxy_idle_timeout string` | ❌ | Délai d'inactivité pour les flux client du proxy UDP avant le nettoyage (correspond à ). (Par défaut : `90s`) |
| `interface` | ❌ | Nom de l'interface WireGuard (par défaut : `newt`) |
| `mtu` | ❌ | MTU pour l'interface WireGuard interne. (Par défaut : `1280`) |
| `native` | ❌ | Utiliser l'interface WireGuard native (par défaut : `false`) |
| `metrics` | ❌ | Activer l'exportateur Prometheus /metrics (par défaut : `false`) |
| `metrics_admin_addr` | ❌ | Lier l'adresse de l'administrateur aux métriques (par défaut : `127.0.0.1:2112`) |
| `metrics_async_bytes` | ❌ | Activer le comptage asynchrone des octets (vider en arrière-plan ; réduction de la surcharge sur le chemin actif, en conséquence) (par défaut : `false`) |
| `health_file` | ❌ | Chemin d'accès au fichier d'intégrité pour la surveillance de la connexion |
| `prefer_endpoint` | ❌ | Privilégier ce point de terminaison pour la connexion (si défini, il remplacera le point de terminaison fourni par le serveur) |
| `region` | ❌ | Attribut facultatif de ressource de région pour la télémétrie et les métriques |
| `name` | ❌ | Nom du site lors du provisionnement à l'aide d'une clé de provisionnement |
| `blueprint_file` | ❌ | Chemin d'accès au fichier de blueprint définissant les ressources et les configurations Pangolin |
| `provisioning_blueprint_file` | ❌ | Chemin d'accès à un fichier de blueprint utilisé uniquement pour le bootstrap |
| `config_file` | ❌ | Chemin d'accès au fichier de configuration JSON dans lequel Newt charge et enregistre les paramètres |
| `ad_ca_cert_path` | ❌ | Chemin d'accès au fichier de certificat CA pour le démon d'authentification (par défaut : `/etc/ssh/ca.pem`) |
| `ad_generate_random_password` | ❌ | Générer un mot de passe aléatoire pour les utilisateurs authentifiés (par défaut : `false`) |
| `ad_pre_shared_key` | ❌ | Clé pré-partagée pour l'authentification par le démon d'authentification. |
| `ad_principals_file` | ❌ | Chemin d'accès au fichier des entités pour le démon d'authentification (par défaut : `/var/run/auth-daemon/principals`) |
| `enforce_hc_cert` | ❌ | Forcer la validation du certificat pour les contrôles d'intégrité (par défaut : `false`) |
| `port` | ❌ | Port permettant aux pairs de se connecter à Newt |
| `pprof` | ❌ | Activer les points de terminaison de débogage pprof sur le serveur d’administration (par défaut : `false`) |
| `otlp` | ❌ | Activer les exportateurs OTLP (métriques/traces) (par défaut : `false`) |
| `updown` | ❌ | Chemin d'accès au script Updown pour les événements d'ajout/suppression de cibles (par défaut : `false`) |


### Exemple de configuration

```yaml
endpoint: "https://app.pangolin.net"
id: "mon-newt-id"
secret: "mon-newt-secret"
log_level: "info"
```

Remarque sur le traitement des options

- Les options de type chaîne de caractères sont transmises à `newt` sous la forme `--flag value`.
- Les options booléennes sont définies comme indicateur (`--flag`) lorsqu’elles sont à `true`.

Autorités de certification TLS

`tls_client_ca` peut être spécifié soit sous la forme d’une chaîne de caractères unique, soit sous la forme d’une liste YAML. Exemples :

```yaml
# fichier unique
tls_client_ca: "/etc/ssl/ca.pem"

# plusieurs fichiers
tls_client_ca:
  - "/etc/ssl/ca.pem"
  - "/etc/ssl/extra-ca.pem"
```

Les entrées sont transmises à `newt` sous la forme d’un drapeau `--tls-client-ca` pour chacune d’entre elles.

## Prérequis

- Un serveur [Pangolin](https://github.com/fosrl/pangolin) en cours d’exécution
- Un site enregistré dans Pangolin avec un Newt-ID et un secret
- Accès au réseau de l'hôte et autorisations WireGuard sur l'hôte Home Assistant

## Comment trouver `newt_id` et `newt_secret`

1. Ouvrez le tableau de bord Pangolin.
2. Sélectionnez le site souhaité ou créez-en un nouveau.
3. Copiez le `newt_id` et le `newt_secret` générés à partir des informations d'accès au site.
4. Utilisez le même `pangolin_endpoint` que celui configuré dans votre installation Pangolin.

## Remarques

- L'extension utilise `host_network` afin que le tunnel puisse fonctionner directement via le réseau hôte.
- Elle nécessite les autorisations `NET_ADMIN` et `SYS_MODULE`.
- Après toute modification de la configuration, l'extension doit être redémarrée.
- `newt_id` et `newt_secret` doivent appartenir au même site Pangolin.
- Ne communiquez pas `newt_secret` à des personnes non autorisées.

## Fonctionnement

Newt se connecte au serveur Pangolin via WebSocket et crée un tunnel WireGuard dans l’espace utilisateur. Toutes les connexions TCP/UDP proxyées sont redirigées vers des services locaux, sans nécessiter de WireGuard au niveau du noyau ni de règles de routage NAT complexes.

## Dépannage

- Vérifiez les journaux de l’extension si le démarrage échoue.
- Assurez-vous que `pangolin_endpoint` est accessible et utilise un certificat TLS valide.
- Assurez-vous que `newt_id` et `newt_secret` proviennent bien du même site Pangolin.
- Définissez `log_level` sur `debug` pour obtenir des informations plus détaillées.
- Si vous modifiez la configuration, arrêtez complètement l'extension et redémarrez-la.

## Informations complémentaires

- [Configuration du site Pangolin](https://docs.pangolin.net/manage/sites/configure-site)
- [Dépôt GitHub de Newt](https://github.com/fosrl/newt)
- [Version 1.13.0 de Newt](https://github.com/fosrl/newt/releases/tag/1.13.0)
