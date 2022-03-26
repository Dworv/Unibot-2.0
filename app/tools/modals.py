
import interactions as inter

def build_review_modal(
    applicant: inter.Member,
    rank: str,
):
    new_role_options = '"Trial", "Member"' if rank == 'None' else '"Member'
    return inter.Modal(
        custom_id='review_modal',
        title=f'Review from {applicant.user.username} (Current Rank: {rank})',
        components=[
            inter.TextInput(
                custom_id='result',
                style=inter.TextStyleType.SHORT, # TODO: change to select menu when added
                label='Result:',
                placeholder=f'Type the new role ({new_role_options}) or "Reapp".',
                min_length=5,
                max_length=6,
                required=True
            ),
            inter.TextInput(
                custom_id='pros',
                style=inter.TextStyleType.PARAGRAPH,
                label='+',
                placeholder='Seperate with new lines',
                required=False
            ),
            inter.TextInput(
                custom_id='procons',
                style=inter.TextStyleType.PARAGRAPH,
                label='+-',
                placeholder='Example line: Repetitive flow, velo is lacking impact, unoriginal song + atmos',
                required=False
            ),
            inter.TextInput(
                custom_id='cons',
                style=inter.TextStyleType.PARAGRAPH,
                label='-',
                placeholder='Please try not to write anything bigger than this text in one single line.',
                required=False
            ),
        ]
    )