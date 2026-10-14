# Como instalar o SkillPacks Free

A instalação é feita copiando as pastas de skills para o diretório reconhecido pelo Claude Code. Não é necessário executar instaladores nem fornecer informações sobre sua máquina.

## Baixe o pacote

1. Abra a página de [Releases](https://github.com/Gabirieu/Skillpacks---Free/releases/latest).
2. Na seção **Assets**, baixe o ZIP com o nome **FGDevs-SkillPacks-Free-v1.2.zip** (ou a versão mais recente).
3. Extraia o conteúdo do ZIP.

Você encontrará uma pasta `skills` com as 10 skills e os respectivos arquivos `SKILL.md`.

## Instalação pessoal

**Windows (PowerShell)**

Na pasta em que você salvou o arquivo ZIP:

```powershell
Expand-Archive -Path ".\FGDevs-SkillPacks-Free-v1.2.zip" -DestinationPath "." -Force
$origem = ".\FGDevs-SkillPacks-Free-v1.2\skills\*"
$destino = Join-Path $HOME ".claude\skills"
New-Item -ItemType Directory -Path $destino -Force | Out-Null
Copy-Item -Path $origem -Destination $destino -Recurse -Force
```

O PowerShell utiliza automaticamente a pasta do usuário atual. Não é necessário substituir nomes ou informar caminhos pessoais.

**macOS e Linux**

Após extrair o ZIP, na pasta da extração:

```bash
mkdir -p ~/.claude/skills
cp -R ./FGDevs-SkillPacks-Free-v1.2/skills/. ~/.claude/skills/
```

## Instalação em um projeto

Na pasta raiz do projeto, use `.claude/skills/` como destino, copiando somente as pastas de skills desejadas.

Exemplo:

```text
.claude/
└── skills/
    ├── cloudflare-deploy/
    │   └── SKILL.md
    └── create-plan/
        └── SKILL.md
```

Não deixe uma segunda pasta `skills` dentro de `.claude/skills/`.

## Utilização

Inicie uma nova sessão do Claude Code e faça uma solicitação relacionada à skill.

```text
Use /cloudflare-deploy para revisar esta configuração de deploy.
```

Se ela não for reconhecida, confira a localização e a presença de `SKILL.md`. A disponibilidade da invocação por barra depende da instalação e da versão do Claude Code.

## Integridade do arquivo

O Release oferece um arquivo `.sha256` para conferir o ZIP baixado. Use `Get-FileHash` no PowerShell ou `shasum -a 256` no macOS/Linux, comparando o resultado com o checksum publicado.

---

[Voltar ao início](../README.md) · [Conhecer as skills](CATALOG.md) · [Baixar pacote](https://github.com/Gabirieu/Skillpacks---Free/releases/latest)
