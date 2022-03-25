
import interactions as inter

def build_review_modal(
    applicant: inter.Member,
    rank: str,
):
    new_role_options = '"Trial", "Member"' if rank == 'None' else '"Member'
    return inter.Modal(
        custom_id='review_modal',
        title=f'Review from {applicant.user.name} (Current Rank: {rank}',
        components=[
            inter.TextInput(
                custom_id='result',
                style=inter.TextStyleType.SHORT, # TODO: change to select menu when added
                label='Result:',
                placeholder='Type the new role ("Trial", "Member") or "Reapp".',
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
                placeholder='Example line: ',
                required=False
            ),
            inter.TextInput(
                custom_id='cons',
                style=inter.TextStyleType.PARAGRAPH,
                label='-',
                placeholder='Try not to write anything more than than this in one line.',
                required=False
            ),
        ]
    )