#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para atualizar o README.md com tarefas dos arquivos 01-FEITO.md, 02-FAZENDO.md e 03-FAZER.md
"""

import re
from pathlib import Path
from datetime import datetime

def read_file(file_path):
    """Lé o conteúdo de um arquivo."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return ""

def extract_tasks(content):
    """Extrai tarefas do conteúdo (linhas que começam com '* ')."""
    tasks = []
    for line in content.split('\n'):
        if line.strip().startswith('* '):
            tasks.append(line.strip())
    return tasks

def update_readme(readme_path, feito_path, fazendo_path, fazer_path):
    """Atualiza o README.md com as tarefas dos arquivos de status."""
    
    # Lé os arquivos
    readme_content = read_file(readme_path)
    feito_content = read_file(feito_path)
    fazendo_content = read_file(fazendo_path)
    fazer_content = read_file(fazer_path)
    
    # Extrai tarefas
    feito_tasks = extract_tasks(feito_content)
    fazendo_tasks = extract_tasks(fazendo_content)
    fazer_tasks = extract_tasks(fazer_content)
    
    # Formata tarefas para o README
    feito_section = '\n'.join(feito_tasks) if feito_tasks else ''
    fazendo_section = '\n'.join(fazendo_tasks) if fazendo_tasks else ''
    fazer_section = '\n'.join(fazer_tasks) if fazer_tasks else ''
    
    # Substitui as seções do README
    readme_updated = re.sub(
        r'(<!-- START_FEITO -->)(.+?)(<!-- END_FEITO -->)',
        f'\\1\n{feito_section}\n\\3',
        readme_content,
        flags=re.DOTALL
    )
    
    readme_updated = re.sub(
        r'(<!-- START_FAZENDO -->)(.+?)(<!-- END_FAZENDO -->)',
        f'\\1\n{fazendo_section}\n\\3',
        readme_updated,
        flags=re.DOTALL
    )
    
    readme_updated = re.sub(
        r'(<!-- START_FAZER -->)(.+?)(<!-- END_FAZER -->)',
        f'\\1\n{fazer_section}\n\\3',
        readme_updated,
        flags=re.DOTALL
    )
    
    # Adiciona timestamp de última atualização
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    readme_updated = re.sub(
        r'(\*Última atualização:)(.*?)\*',
        f'\\1 {timestamp} *',
        readme_updated
    )
    
    # Escreve o README atualizado
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(readme_updated)
    
    print(f'README.md atualizado com sucesso em {timestamp}')

if __name__ == '__main__':
    # Define os caminhos
    repo_dir = Path(__file__).parent.parent.parent
    readme_path = repo_dir / 'README.md'
    feito_path = repo_dir / '01-FEITO.md'
    fazendo_path = repo_dir / '02-FAZENDO.md'
    fazer_path = repo_dir / '03-FAZER.md'
    
    # Atualiza o README
    update_readme(readme_path, feito_path, fazendo_path, fazer_path)
